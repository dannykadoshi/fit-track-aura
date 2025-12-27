from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Workout, Exercise, WorkoutExercise
from .forms import WorkoutForm, WorkoutExerciseFormSet


def home(request):
    """Homepage view"""
    return render(request, 'pages/home.html')


@login_required
def dashboard(request):
    """User dashboard view"""
    context = {
        'workouts_count': request.user.workouts.count(),
        'recent_workouts': request.user.workouts.all()[:5],
        'active_goals': request.user.goals.filter(is_completed=False)[:3],
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