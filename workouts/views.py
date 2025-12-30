from django.shortcuts import render, redirect, get_object_or_404
from goals.badge_utils import check_and_award_badges
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Workout, WorkoutExercise, Exercise
from .forms import WorkoutForm, WorkoutExerciseFormSet, ExerciseForm
from goals.models import Goal


def home(request):
    """Landing page view"""
    return render(request, 'pages/home.html')


@login_required
def dashboard(request):
    """Dashboard view with user statistics"""
    user = request.user
    today = timezone.now().date()
    
    # Get workouts
    workouts = Workout.objects.filter(user=user).order_by('-date')
    workouts_count = workouts.count()
    
    # This month's workouts
    first_day_of_month = today.replace(day=1)
    workouts_this_month = workouts.filter(date__gte=first_day_of_month).count()
    
    # Total training time this month
    total_time = workouts.filter(date__gte=first_day_of_month).aggregate(
        total=Sum('duration')
    )['total'] or 0
    
    # Calculate workout streak
    current_streak = 0
    best_streak = 0
    temp_streak = 0
    
    if workouts.exists():
        workout_dates = set(workouts.values_list('date', flat=True))
        check_date = today
        
        # Current streak
        while check_date in workout_dates:
            current_streak += 1
            check_date -= timedelta(days=1)
        
        # Best streak
        all_dates = sorted(workout_dates, reverse=True)
        if all_dates:
            temp_streak = 1
            for i in range(len(all_dates) - 1):
                if (all_dates[i] - all_dates[i + 1]).days == 1:
                    temp_streak += 1
                    best_streak = max(best_streak, temp_streak)
                else:
                    temp_streak = 1
            best_streak = max(best_streak, temp_streak, current_streak)
    
    # Get active goals
    active_goals = Goal.objects.filter(user=user, is_completed=False).order_by('target_date')
    goals_count = active_goals.count()
    
    # Calculate average goal progress
    if goals_count > 0:
        total_progress = 0
        valid_goals = 0
        for goal in active_goals:
            goal_progress = goal.progress_percentage
            total_progress += goal_progress
            valid_goals += 1
        avg_progress = total_progress / valid_goals if valid_goals > 0 else 0
    else:
        avg_progress = 0
    
    # Get goals with progress for template
    goals_with_progress = []
    for goal in active_goals[:3]:
        goal.progress = goal.progress_percentage
        goals_with_progress.append(goal)
    
    # Recent workouts
    recent_workouts = workouts[:5]
    for workout in recent_workouts:
        workout.total_exercises = workout.workout_exercises.count()
    
    # Weekly activity data for chart
    week_start = today - timedelta(days=today.weekday())  # Monday
    week_data = []
    day_labels = []
    
    for i in range(7):
        day = week_start + timedelta(days=i)
        day_workouts = workouts.filter(date=day)
        total_duration = day_workouts.aggregate(total=Sum('duration'))['total'] or 0
        
        week_data.append(total_duration)
        day_labels.append(day.strftime('%a'))  # Mon, Tue, Wed, etc.
    
    # Weekly stats
    weekly_total = sum(week_data)
    weekly_average = weekly_total / 7 if weekly_total > 0 else 0
    max_day_duration = max(week_data) if week_data else 0
    max_day_index = week_data.index(max_day_duration) if max_day_duration > 0 else None
    most_active_day = day_labels[max_day_index] if max_day_index is not None else None
    
    context = {
        'workouts_count': workouts_count,
        'workouts_this_month': workouts_this_month,
        'total_time': total_time,
        'current_streak': current_streak,
        'best_streak': best_streak,
        'active_goals': goals_with_progress,
        'goals_count': goals_count,  # <-- ADDED THIS!
        'goals_progress': int(avg_progress),
        'recent_workouts': recent_workouts,
        # Chart data
        'week_labels': day_labels,
        'week_data': week_data,
        'weekly_total': weekly_total,
        'weekly_average': int(weekly_average),
        'most_active_day': most_active_day,
        'max_day_duration': int(max_day_duration),
    }
    
    return render(request, 'pages/dashboard.html', context)


@login_required
def workout_list(request):
    """List all workouts for the logged-in user"""
    workouts = Workout.objects.filter(user=request.user).order_by('-date')
    
    # Add exercise count to each workout
    for workout in workouts:
        workout.total_exercises = workout.workout_exercises.count()
    
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})


@login_required
def workout_detail(request, pk):
    """Display a single workout"""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    return render(request, 'workouts/workout_detail.html', {'workout': workout})


@login_required
def workout_create(request):
    """Create a new workout"""
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        formset = WorkoutExerciseFormSet(request.POST, form_kwargs={'user': request.user})
        
        if form.is_valid() and formset.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            
            formset.instance = workout
            formset.save()
            
            # Check for new badges
            check_and_award_badges(request.user, request)
            
            messages.success(request, f'Workout "{workout.title}" created successfully! 🎉')
            return redirect('dashboard')
    else:
        form = WorkoutForm()
        formset = WorkoutExerciseFormSet(form_kwargs={'user': request.user})
    
    return render(request, 'workouts/workout_form.html', {
        'form': form,
        'formset': formset,
        'action': 'Create'
    })


@login_required
def workout_update(request, pk):
    """Update an existing workout"""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        formset = WorkoutExerciseFormSet(request.POST, instance=workout, form_kwargs={'user': request.user})
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            
            messages.success(request, f'Workout "{workout.title}" updated successfully! ✅')
            return redirect('dashboard')
    else:
        form = WorkoutForm(instance=workout)
        formset = WorkoutExerciseFormSet(instance=workout, form_kwargs={'user': request.user})
    
    return render(request, 'workouts/workout_form.html', {
        'form': form,
        'formset': formset,
        'action': 'Update',
        'workout': workout
    })


@login_required
def workout_delete(request, pk):
    """Delete a workout"""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)
    
    if request.method == 'POST':
        workout_title = workout.title
        workout.delete()
        messages.success(request, f'Workout "{workout_title}" deleted successfully! 🗑️')
        return redirect('dashboard')
    
    return render(request, 'workouts/workout_confirm_delete.html', {'workout': workout})


def faq(request):
    """FAQ page view"""
    return render(request, 'pages/faq.html')


def about(request):
    """About page view"""
    return render(request, 'pages/about.html')


@login_required
def exercise_library(request):
    """Display all exercises (default + user's custom)"""
    # Get default exercises
    default_exercises = Exercise.objects.filter(is_custom=False).order_by('category', 'name')
    
    # Get user's custom exercises
    custom_exercises = Exercise.objects.filter(created_by=request.user, is_custom=True).order_by('category', 'name')
    
    context = {
        'default_exercises': default_exercises,
        'custom_exercises': custom_exercises,
    }
    
    return render(request, 'workouts/exercise_library.html', context)


@login_required
def exercise_create(request):
    """Create a custom exercise"""
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.created_by = request.user
            exercise.is_custom = True
            exercise.save()
            
            # Check for new badges
            check_and_award_badges(request.user, request)
            
            messages.success(request, f'Exercise "{exercise.name}" created successfully! ✨')
            return redirect('exercise_library')
    else:
        form = ExerciseForm()
    
    return render(request, 'workouts/exercise_form.html', {'form': form, 'action': 'Create'})


@login_required
def exercise_update(request, pk):
    """Update a custom exercise (only user's own)"""
    exercise = get_object_or_404(Exercise, pk=pk, created_by=request.user, is_custom=True)
    
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            messages.success(request, f'Exercise "{exercise.name}" updated successfully! ✅')
            return redirect('exercise_library')
    else:
        form = ExerciseForm(instance=exercise)
    
    return render(request, 'workouts/exercise_form.html', {'form': form, 'action': 'Update', 'exercise': exercise})


@login_required
def exercise_delete(request, pk):
    """Delete a custom exercise (only user's own)"""
    exercise = get_object_or_404(Exercise, pk=pk, created_by=request.user, is_custom=True)
    
    if request.method == 'POST':
        exercise_name = exercise.name
        exercise.delete()
        messages.success(request, f'Exercise "{exercise_name}" deleted successfully! 🗑️')
        return redirect('exercise_library')
    
    return render(request, 'workouts/exercise_confirm_delete.html', {'exercise': exercise})


@login_required
def badges(request):
    """Display user's badges and available badges to unlock"""
    from goals.models import Badge
    
    # Get user's earned badges
    earned_badges = Badge.objects.filter(user=request.user)
    earned_badge_types = set(earned_badges.values_list('badge_type', flat=True))
    
    # All possible badges
    all_badge_types = [
        ('first_workout', '🎯 First Step', 'Complete your first workout'),
        ('10_workouts', '💪 Getting Strong', 'Log 10 workouts'),
        ('7_day_streak', '🔥 On Fire', 'Maintain a 7-day workout streak'),
        ('first_goal', '⭐ Goal Crusher', 'Complete your first goal'),
        ('custom_exercise', '✨ Innovator', 'Create a custom exercise'),
        ('50_workouts', '🚀 Dedicated', 'Log 50 workouts'),
        ('30_day_streak', '👑 Champion', 'Maintain a 30-day workout streak'),
    ]
    
    # Separate earned and locked badges
    earned_list = []
    locked_list = []
    
    for badge_type, name, description in all_badge_types:
        badge_data = {
            'type': badge_type,
            'icon': name.split()[0],  # Get emoji
            'name': ' '.join(name.split()[1:]),  # Get name without emoji
            'description': description,
        }
        
        if badge_type in earned_badge_types:
            # Add earned date
            badge_obj = earned_badges.get(badge_type=badge_type)
            badge_data['earned_date'] = badge_obj.earned_date
            earned_list.append(badge_data)
        else:
            locked_list.append(badge_data)
    
    context = {
        'earned_badges': earned_list,
        'locked_badges': locked_list,
        'total_earned': len(earned_list),
        'total_badges': len(all_badge_types),
    }
    
    return render(request, 'pages/badges.html', context)
