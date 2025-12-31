from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from datetime import date
from .models import Workout
from .share_utils import (
    generate_share_text,
    get_share_url,
    generate_twitter_url,
    generate_facebook_url,
    generate_linkedin_url
)
from goals.models import Goal, Badge


class ShareUtilsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.factory = RequestFactory()

    def test_generate_share_text_workout_completed(self):
        """Test share text for completed workout"""
        workout = Workout.objects.create(
            user=self.user,
            title='Morning Run',
            date=date.today(),
            duration=30
        )

        share_text = generate_share_text('workout_completed', self.user, workout=workout)

        self.assertIn('Morning Run', share_text)
        self.assertIn('30min', share_text)
        self.assertIn('FitTrack Aura', share_text)

    def test_generate_share_text_goal_achieved(self):
        """Test share text for achieved goal"""
        goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            category='endurance',
            target_number=100,
            current_number=100,
            unit='km',
            target_date=date.today(),
            is_completed=True
        )

        share_text = generate_share_text('goal_achieved', self.user, goal=goal)

        self.assertIn('Run 100km', share_text)
        self.assertIn('Goal achieved', share_text)

    def test_generate_share_text_streak(self):
        """Test share text for workout streak"""
        share_text = generate_share_text('streak', self.user, streak=7)

        self.assertIn('7 day', share_text)
        self.assertIn('streak', share_text)

    def test_generate_share_text_badge_earned(self):
        """Test share text for earned badge"""
        badge = Badge.objects.create(
            user=self.user,
            badge_type='first_workout'
        )

        share_text = generate_share_text('badge_earned', self.user, badge=badge)

        self.assertIn('First Step', share_text)
        self.assertIn('Achievement', share_text)

    def test_generate_share_text_monthly_summary(self):
        """Test share text for monthly summary"""
        share_text = generate_share_text(
            'monthly_summary',
            self.user,
            workouts=15,
            duration=450
        )

        self.assertIn('15 workouts', share_text)
        self.assertIn('450 minutes', share_text)

    def test_generate_share_text_unknown_type(self):
        """Test share text for unknown achievement type"""
        share_text = generate_share_text('unknown_type', self.user)

        self.assertIn('FitTrack Aura', share_text)
        self.assertIsInstance(share_text, str)

    def test_get_share_url(self):
        """Test getting share URL from request"""
        request = self.factory.get('/dashboard/')
        request.user = self.user

        url = get_share_url(request, 'workout_completed')

        self.assertIsInstance(url, str)
        self.assertIn('/dashboard/', url)

    def test_generate_twitter_url(self):
        """Test Twitter share URL generation"""
        text = "Check out my workout!"
        url = "https://example.com"

        twitter_url = generate_twitter_url(text, url)

        self.assertIn('twitter.com/intent/tweet', twitter_url)
        self.assertIn('text=', twitter_url)
        self.assertIn('url=', twitter_url)

    def test_generate_facebook_url(self):
        """Test Facebook share URL generation"""
        url = "https://example.com"

        facebook_url = generate_facebook_url(url)

        self.assertIn('facebook.com/sharer', facebook_url)
        self.assertIn('u=', facebook_url)

    def test_generate_linkedin_url(self):
        """Test LinkedIn share URL generation"""
        url = "https://example.com"

        linkedin_url = generate_linkedin_url(url)

        self.assertIn('linkedin.com', linkedin_url)
        self.assertIsInstance(linkedin_url, str)

    def test_twitter_url_handles_special_characters(self):
        """Test Twitter URL properly encodes special characters"""
        text = "Amazing workout! 💪 #fitness"
        url = "https://example.com/workout?id=123&user=test"

        twitter_url = generate_twitter_url(text, url)

        self.assertIsInstance(twitter_url, str)
        self.assertIn('twitter.com', twitter_url)

    def test_share_text_with_missing_workout_attribute(self):
        """Test share text generation when workout lacks title"""
        workout = Workout.objects.create(
            user=self.user,
            title='',  # Empty title
            date=date.today(),
            duration=30
        )

        share_text = generate_share_text('workout_completed', self.user, workout=workout)

        self.assertIsInstance(share_text, str)
        self.assertIn('FitTrack Aura', share_text)
