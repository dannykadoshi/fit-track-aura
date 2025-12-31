from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date, timedelta
from .models import Workout
from .utils import calculate_workout_streak


class WorkoutStreakTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_no_workouts_returns_zero_streak(self):
        """Test streak calculation with no workouts"""
        result = calculate_workout_streak(self.user)
        self.assertEqual(result['current_streak'], 0)
        self.assertEqual(result['best_streak'], 0)
        
    def test_single_workout_today(self):
        """Test streak with single workout today"""
        Workout.objects.create(
            user=self.user,
            title='Today Workout',
            date=date.today(),
            duration=30
        )
        
        result = calculate_workout_streak(self.user)
        self.assertEqual(result['current_streak'], 1)
        self.assertEqual(result['best_streak'], 1)
        
    def test_consecutive_workouts(self):
        """Test streak with consecutive daily workouts"""
        today = date.today()
        for i in range(5):
            Workout.objects.create(
                user=self.user,
                title=f'Workout {i}',
                date=today - timedelta(days=i),
                duration=30
            )
        
        result = calculate_workout_streak(self.user)
        self.assertEqual(result['current_streak'], 5)
        self.assertEqual(result['best_streak'], 5)
        
    def test_broken_streak(self):
        """Test streak with gap in workouts"""
        today = date.today()
        
        # Recent workouts (3 day streak)
        for i in range(3):
            Workout.objects.create(
                user=self.user,
                title=f'Recent Workout {i}',
                date=today - timedelta(days=i),
                duration=30
            )
        
        # Gap of 2 days
        
        # Older workouts (5 day streak)
        for i in range(5):
            Workout.objects.create(
                user=self.user,
                title=f'Old Workout {i}',
                date=today - timedelta(days=i + 5),
                duration=30
            )
        
        result = calculate_workout_streak(self.user)
        self.assertEqual(result['current_streak'], 3)
        self.assertEqual(result['best_streak'], 5)
        
    def test_workout_yesterday_counts_as_current_streak(self):
        """Test that yesterday's workout counts for current streak"""
        yesterday = date.today() - timedelta(days=1)
        Workout.objects.create(
            user=self.user,
            title='Yesterday Workout',
            date=yesterday,
            duration=30
        )
        
        result = calculate_workout_streak(self.user)
        self.assertEqual(result['current_streak'], 1)
        
    def test_old_workout_no_current_streak(self):
        """Test old workout doesn't count as current streak"""
        old_date = date.today() - timedelta(days=5)
        Workout.objects.create(
            user=self.user,
            title='Old Workout',
            date=old_date,
            duration=30
        )
        
        result = calculate_workout_streak(self.user)
        self.assertEqual(result['current_streak'], 0)
        self.assertEqual(result['best_streak'], 1)
        
    def test_multiple_workouts_same_day(self):
        """Test multiple workouts on same day count as one day"""
        today = date.today()
        
        # Create 2 workouts today
        Workout.objects.create(
            user=self.user,
            title='Morning Workout',
            date=today,
            duration=30
        )
        Workout.objects.create(
            user=self.user,
            title='Evening Workout',
            date=today,
            duration=45
        )
        
        result = calculate_workout_streak(self.user)
        self.assertEqual(result['current_streak'], 1)
        self.assertEqual(result['best_streak'], 1)
        
    def test_longest_streak_in_past(self):
        """Test best streak recognition when it's in the past"""
        today = date.today()
        
        # Current: 2 days
        for i in range(2):
            Workout.objects.create(
                user=self.user,
                title=f'Current {i}',
                date=today - timedelta(days=i),
                duration=30
            )
        
        # Gap
        
        # Past: 7 days (best streak)
        for i in range(7):
            Workout.objects.create(
                user=self.user,
                title=f'Past {i}',
                date=today - timedelta(days=i + 4),
                duration=30
            )
        
        result = calculate_workout_streak(self.user)
        self.assertEqual(result['current_streak'], 2)
        self.assertEqual(result['best_streak'], 7)
