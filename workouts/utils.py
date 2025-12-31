from datetime import date, timedelta


def calculate_workout_streak(user):
    """
    Calculate the current workout streak for a user.
    Returns a dictionary with current_streak and best_streak.
    """
    from workouts.models import Workout

    # Get all workout dates for this user, ordered by date (oldest first)
    workout_dates = Workout.objects.filter(user=user).values_list('date', flat=True).order_by('date').distinct()

    if not workout_dates:
        return {'current_streak': 0, 'best_streak': 0}

    # Convert to list and sort in reverse (newest first)
    dates = sorted(list(set(workout_dates)), reverse=True)

    # Calculate current streak
    current_streak = 0
    today = date.today()

    # Check if there's a workout today or yesterday (to count ongoing streaks)
    if dates[0] >= today - timedelta(days=1):
        current_streak = 1
        current_date = dates[0]

        # Count consecutive days
        for i in range(1, len(dates)):
            # Check if this date is exactly 1 day before the previous date
            if dates[i] == current_date - timedelta(days=1):
                current_streak += 1
                current_date = dates[i]
            else:
                # Streak broken
                break

    # Calculate best streak (all-time)
    best_streak = 0
    temp_streak = 1

    # Go through dates in chronological order (oldest to newest)
    dates_chronological = sorted(dates)

    for i in range(1, len(dates_chronological)):
        if dates_chronological[i] == dates_chronological[i-1] + timedelta(days=1):
            temp_streak += 1
            best_streak = max(best_streak, temp_streak)
        else:
            temp_streak = 1

    best_streak = max(best_streak, temp_streak)

    return {
        'current_streak': current_streak,
        'best_streak': best_streak
    }
