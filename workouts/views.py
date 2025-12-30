from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import timedelta, datetime
from .models import Workout, WorkoutExercise, Exercise
from .forms import WorkoutForm, WorkoutExerciseFormSet
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
        workout.total_exercises = workout.exercises.count()
    
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
        formset = WorkoutExerciseFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            
            formset.instance = workout
            formset.save()
            
            messages.success(request, f'Workout "{workout.title}" created successfully! 🎉')
            return redirect('dashboard')
    else:
        form = WorkoutForm()
        formset = WorkoutExerciseFormSet()
    
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
        formset = WorkoutExerciseFormSet(request.POST, instance=workout)
        
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            
            messages.success(request, f'Workout "{workout.title}" updated successfully! ✅')
            return redirect('dashboard')
    else:
        form = WorkoutForm(instance=workout)
        formset = WorkoutExerciseFormSet(instance=workout)
    
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
