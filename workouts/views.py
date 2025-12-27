from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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