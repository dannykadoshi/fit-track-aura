

def generate_share_text(achievement_type, user, **kwargs):
    """Generate shareable text for different achievement types"""

    if achievement_type == 'workout_completed':
        workout = kwargs.get('workout')
        return (
            f"💪 Just completed '{workout.title}' on FitTrack Aura! "
            f"{workout.duration}min of training done! #fitness #workout"
        )

    elif achievement_type == 'goal_achieved':
        goal = kwargs.get('goal')
        return (
            f"🎯 Goal achieved on FitTrack Aura: {goal.title}! "
            f"Another milestone reached! #fitnessgoals #success"
        )

    elif achievement_type == 'streak':
        streak = kwargs.get('streak')
        return f"🔥 {streak} day workout streak on FitTrack Aura! Consistency is key! #fitnessmotivation #streak"

    elif achievement_type == 'badge_earned':
        badge = kwargs.get('badge')
        return (
            f"🏆 Achievement unlocked on FitTrack Aura: {badge.badge_name}! "
            f"{badge.badge_description} #achievement #fitness"
        )

    elif achievement_type == 'monthly_summary':
        workouts = kwargs.get('workouts')
        duration = kwargs.get('duration')
        return (
            f"📊 This month on FitTrack Aura: {workouts} workouts, "
            f"{duration} minutes of training! Keep pushing! #fitnessjourney"
        )

    return "Check out my progress on FitTrack Aura! 💪 #fitness"


def get_share_url(request, achievement_type, **kwargs):
    """Get the current page URL for sharing"""
    return request.build_absolute_uri()


def generate_twitter_url(text, url):
    """Generate Twitter/X share URL"""
    from urllib.parse import quote
    return f"https://twitter.com/intent/tweet?text={quote(text)}&url={quote(url)}"


def generate_facebook_url(url):
    """Generate Facebook share URL"""
    from urllib.parse import quote
    return f"https://www.facebook.com/sharer/sharer.php?u={quote(url)}"


def generate_linkedin_url(url):
    """Generate LinkedIn share URL"""
    from urllib.parse import quote
    return f"https://www.linkedin.com/sharing/share-offsite/?url={quote(url)}"


def generate_whatsapp_url(text):
    """Generate WhatsApp share URL"""
    from urllib.parse import quote
    return f"https://wa.me/?text={quote(text)}"
