from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Goal
from .forms import GoalForm
from .badge_utils import check_and_award_badges


@login_required
def goal_list(request):
    """List all goals for the logged-in user"""
    active_goals = request.user.goals.filter(is_completed=False).order_by('target_date')
    completed_goals = request.user.goals.filter(is_completed=True).order_by('-completed_date')

    context = {
        'active_goals': active_goals,
        'completed_goals': completed_goals,
    }
    return render(request, 'goals/goal_list.html', context)


@login_required
def goal_create(request):
    """Create a new goal"""
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Goal created successfully! 🎯')
            return redirect('goal_list')
    else:
        form = GoalForm()

    context = {
        'form': form,
    }
    return render(request, 'goals/goal_form.html', context)


@login_required
def goal_update(request, pk):
    """Update an existing goal"""
    goal = get_object_or_404(Goal, pk=pk, user=request.user)

    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Goal updated successfully! ✅')
            return redirect('goal_list')
    else:
        form = GoalForm(instance=goal)

    context = {
        'form': form,
        'goal': goal,
    }
    return render(request, 'goals/goal_form.html', context)


@login_required
def goal_delete(request, pk):
    """Delete a goal"""
    goal = get_object_or_404(Goal, pk=pk, user=request.user)

    if request.method == 'POST':
        goal.delete()
        messages.success(request, 'Goal deleted successfully! 🗑️')
        return redirect('goal_list')

    context = {
        'goal': goal,
    }
    return render(request, 'goals/goal_confirm_delete.html', context)


@login_required
def goal_complete(request, pk):
    """Mark a goal as complete"""
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    goal.mark_complete()
    
    # Check for new badges
    check_and_award_badges(request.user, request)
    
    messages.success(request, f'Goal "{goal.title}" marked as complete! 🎉')
    return redirect('goal_list')


@login_required
def export_goals_pdf(request):
    """Export user's goals to PDF"""
    from django.http import HttpResponse
    from workouts.pdf_utils import generate_goals_pdf
    from datetime import datetime
    
    goals = Goal.objects.filter(user=request.user).order_by('-created_at')
    
    # Generate PDF
    pdf_buffer = generate_goals_pdf(goals, request.user)
    
    # Create response
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    filename = f"FitTrack_Goals_{datetime.now().strftime('%Y%m%d')}.pdf"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    messages.success(request, f'Goals exported successfully! 📄')
    
    return response
