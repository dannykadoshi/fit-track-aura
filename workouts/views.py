from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from datetime import date, timedelta
from .models import Workout, Exercise, WorkoutExercise
from .forms import WorkoutForm, WorkoutExerciseFormSet
from .utils import calculate_workout_streak


def home(request):
    """Homepage view"""
    return render(request, 'pages/home.html')


@login_required
def dashboard(request):
    """User dashboard view"""
    # Get current month's workouts
    today = date.today()
    first_day_of_month = today.replace(day=1)

    workouts_this_month = Workout.objects.filter(
        user=request.user,
        date__gte=first_day_of_month,
        date__lte=today
    ).count()

    # Total training time this month
    total_time = Workout.objects.filter(
        user=request.user,
        date__gte=first_day_of_month,
        date__lte=today
    ).aggregate(Sum('duration'))['duration__sum'] or 0

    # Get active goals
    active_goals = request.user.goals.filter(is_completed=False)
    goals_count = active_goals.count()

    # Calculate average goal progress
    if goals_count > 0:
        total_progress = 0
        valid_goals = 0
        for goal in active_goals:
            try:
                # Convert string values to float for comparison
                target = float(goal.target_value) if goal.target_value else 0
                current = float(goal.current_value) if goal.current_value else 0

                if target > 0:
                    goal_progress = (current / target) * 100
                    total_progress += min(goal_progress, 100)  # Cap at 100%
                    valid_goals += 1
            except (ValueError, TypeError):
                # If conversion fails, skip this goal
                continue

        avg_progress = total_progress / valid_goals if valid_goals > 0 else 0
    else:
        avg_progress = 0

    # Get recent workouts
    recent_workouts = request.user.workouts.all()[:5]

    # Calculate workout streak
    streak_data = calculate_workout_streak(request.user)

    # Add progress property to each goal for the template
    goals_with_progress = []
    for goal in active_goals[:3]:
        try:
            # Convert string values to float
            target = float(goal.target_value) if goal.target_value else 0
            current = float(goal.current_value) if goal.current_value else 0

            if target > 0:
                goal.progress = min(int((current / target) * 100), 100)
            else:
                goal.progress = 0
        except (ValueError, TypeError):
            goal.progress = 0

        goals_with_progress.append(goal)

    context = {
        'workouts_count': request.user.workouts.count(),
        'workouts_this_month': workouts_this_month,
        'total_time': total_time,
        'goals_progress': round(avg_progress, 1),
        'recent_workouts': recent_workouts,
        'active_goals': goals_with_progress,
        'current_streak': streak_data['current_streak'],
        'best_streak': streak_data['best_streak'],
    }

    return render(request, 'pages/dashboard.html', context)


@login_required
def workout_list(request):
    """List all workouts for the logged-in user"""
    workouts = request.user.workouts.all()

    # Get filter parameters
    search_query = request.GET.get('search', '')

    # Apply search filter
    if search_query:
        workouts = workouts.filter(title__icontains=search_query)

    context = {
        'workouts': workouts,
        'search_query': search_query,
    }

    return render(request, 'workouts/workout_list.html', context)


@login_required
def workout_detail(request, pk):
    """View a single workout in detail"""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    context = {
        'workout': workout,
    }

    return render(request, 'workouts/workout_detail.html', context)


@login_required
def workout_create(request):
    """Create a new workout"""
    if request.method == 'POST':
        workout_form = WorkoutForm(request.POST)
        formset = WorkoutExerciseFormSet(request.POST)

        if workout_form.is_valid() and formset.is_valid():
            # Save the workout
            workout = workout_form.save(commit=False)
            workout.user = request.user
            workout.save()

            # Save the exercises
            formset.instance = workout
            formset.save()

            messages.success(request, 'Workout logged successfully! 🎉')
            return redirect('workout_detail', pk=workout.pk)
    else:
        workout_form = WorkoutForm()
        formset = WorkoutExerciseFormSet()

    context = {
        'workout_form': workout_form,
        'formset': formset,
        'exercises': Exercise.objects.all(),
    }

    return render(request, 'workouts/workout_form.html', context)


@login_required
def workout_update(request, pk):
    """Update an existing workout"""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    if request.method == 'POST':
        workout_form = WorkoutForm(request.POST, instance=workout)
        formset = WorkoutExerciseFormSet(request.POST, instance=workout)

        if workout_form.is_valid() and formset.is_valid():
            workout_form.save()
            formset.save()

            messages.success(request, 'Workout updated successfully! ✅')
            return redirect('workout_detail', pk=workout.pk)
    else:
        workout_form = WorkoutForm(instance=workout)
        formset = WorkoutExerciseFormSet(instance=workout)

    context = {
        'workout_form': workout_form,
        'formset': formset,
        'workout': workout,
        'exercises': Exercise.objects.all(),
    }

    return render(request, 'workouts/workout_form.html', context)


@login_required
def workout_delete(request, pk):
    """Delete a workout"""
    workout = get_object_or_404(Workout, pk=pk, user=request.user)

    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'Workout deleted successfully! 🗑️')
        return redirect('workout_list')

    context = {
        'workout': workout,
    }

    return render(request, 'workouts/workout_confirm_delete.html', context)
