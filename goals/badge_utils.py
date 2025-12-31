from django.contrib import messages
from .models import Badge
from workouts.models import Workout, Exercise


def check_and_award_badges(user, request=None):
    """
    Check if user has earned any badges and award them
    Returns list of newly earned badges
    """
    newly_earned = []

    # 🎯 First Workout
    if not Badge.objects.filter(user=user, badge_type='first_workout').exists():
        if Workout.objects.filter(user=user).count() >= 1:
            badge = Badge.objects.create(user=user, badge_type='first_workout')
            newly_earned.append(badge)

    # 💪 10 Workouts
    if not Badge.objects.filter(user=user, badge_type='10_workouts').exists():
        if Workout.objects.filter(user=user).count() >= 10:
            badge = Badge.objects.create(user=user, badge_type='10_workouts')
            newly_earned.append(badge)

    # 🚀 50 Workouts
    if not Badge.objects.filter(user=user, badge_type='50_workouts').exists():
        if Workout.objects.filter(user=user).count() >= 50:
            badge = Badge.objects.create(user=user, badge_type='50_workouts')
            newly_earned.append(badge)

    # ⭐ First Goal
    if not Badge.objects.filter(user=user, badge_type='first_goal').exists():
        from goals.models import Goal
        if Goal.objects.filter(user=user, is_completed=True).count() >= 1:
            badge = Badge.objects.create(user=user, badge_type='first_goal')
            newly_earned.append(badge)

    # ✨ Custom Exercise
    if not Badge.objects.filter(user=user, badge_type='custom_exercise').exists():
        if Exercise.objects.filter(created_by=user, is_custom=True).count() >= 1:
            badge = Badge.objects.create(user=user, badge_type='custom_exercise')
            newly_earned.append(badge)

    # 🔥 7-Day Streak (check current streak from dashboard calculation)
    if not Badge.objects.filter(user=user, badge_type='7_day_streak').exists():
        current_streak = calculate_current_streak(user)
        if current_streak >= 7:
            badge = Badge.objects.create(user=user, badge_type='7_day_streak')
            newly_earned.append(badge)

    # 👑 30-Day Streak
    if not Badge.objects.filter(user=user, badge_type='30_day_streak').exists():
        current_streak = calculate_current_streak(user)
        if current_streak >= 30:
            badge = Badge.objects.create(user=user, badge_type='30_day_streak')
            newly_earned.append(badge)

    # Show success messages for newly earned badges
    if request and newly_earned:
        for badge in newly_earned:
            messages.success(
                request,
                f'🎉 Achievement Unlocked: {badge.badge_icon} {badge.badge_name}!',
                extra_tags='badge-earned'
            )

    return newly_earned


def calculate_current_streak(user):
    """Calculate user's current workout streak"""
    from datetime import timedelta
    from django.utils import timezone

    today = timezone.now().date()
    workouts = Workout.objects.filter(user=user).order_by('-date')

    if not workouts.exists():
        return 0

    workout_dates = set(workouts.values_list('date', flat=True))
    current_streak = 0
    check_date = today

    while check_date in workout_dates:
        current_streak += 1
        check_date -= timedelta(days=1)

    return current_streak
