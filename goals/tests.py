from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Goal
from datetime import date, timedelta


class GoalModelTest(TestCase):
    """Test cases for Goal model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_goal_creation(self):
        """Test that a goal can be created"""
        goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            target_value='100km',
            target_date=date.today() + timedelta(days=30)
        )
        self.assertEqual(goal.title, 'Run 100km')
        self.assertFalse(goal.is_completed)

    def test_goal_mark_complete(self):
        """Test marking a goal as complete"""
        goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            target_value='100km',
            target_date=date.today() + timedelta(days=30)
        )

        goal.mark_complete()

        self.assertTrue(goal.is_completed)
        self.assertIsNotNone(goal.completed_date)


class GoalViewTest(TestCase):
    """Test cases for Goal views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_goal_list_requires_login(self):
        """Test that goal list requires authentication"""
        response = self.client.get(reverse('goal_list'))
        self.assertEqual(response.status_code, 302)

    def test_goal_list_view_authenticated(self):
        """Test goal list view when logged in"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('goal_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/goal_list.html')


class GoalCompleteTest(TestCase):
    """Test cases for completing goals"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            target_value='100km',
            target_date=date.today() + timedelta(days=30)
        )

    def test_complete_goal(self):
        """Test completing a goal"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('goal_complete', args=[self.goal.pk])
        )

        # Should redirect
        self.assertEqual(response.status_code, 302)

        # Goal should be marked complete
        self.goal.refresh_from_db()
        self.assertTrue(self.goal.is_completed)
        self.assertIsNotNone(self.goal.completed_date)

    def test_user_cannot_complete_other_users_goal(self):
        """Test users can't complete goals they don't own"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )

        self.client.login(username='otheruser', password='testpass123')
        response = self.client.post(
            reverse('goal_complete', args=[self.goal.pk])
        )

        # Should get 404 or redirect
        self.assertIn(response.status_code, [302, 404])

        # Goal should not be completed
        self.goal.refresh_from_db()
        self.assertFalse(self.goal.is_completed)


class GoalUpdateTest(TestCase):
    """Test cases for updating goals"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            target_number=100,
            current_number=0,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

    def test_update_goal_progress(self):
        """Test updating goal progress"""
        self.client.login(username='testuser', password='testpass123')

        updated_data = {
            'title': 'Run 100km',
            'category': 'endurance',
            'target_number': 100,
            'current_number': 50,
            'unit': 'km',
            'target_date': self.goal.target_date
        }

        response = self.client.post(
            reverse('goal_update', args=[self.goal.pk]),
            data=updated_data
        )

        # Should redirect
        self.assertEqual(response.status_code, 302)

        # Progress should be updated
        self.goal.refresh_from_db()
        self.assertEqual(self.goal.current_number, 50)


class BadgeModelTests(TestCase):
    """Test cases for Badge model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_badge_creation(self):
        """Test creating a badge"""
        from .models import Badge

        badge = Badge.objects.create(
            user=self.user,
            badge_type='first_workout'
        )

        self.assertEqual(badge.user, self.user)
        self.assertEqual(badge.badge_type, 'first_workout')
        self.assertIsNotNone(badge.earned_date)

    def test_badge_string_representation(self):
        """Test badge string representation"""
        from .models import Badge

        badge = Badge.objects.create(
            user=self.user,
            badge_type='first_workout'
        )

        # Badge __str__ returns display name - username
        expected_str = f'{badge.get_badge_type_display()} - {self.user.username}'
        self.assertEqual(str(badge), expected_str)


class BadgeUtilsTests(TestCase):
    """Test cases for badge utility functions"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_first_workout_badge_awarded(self):
        """Test first workout badge is awarded"""
        from workouts.models import Workout
        from .badge_utils import check_and_award_badges

        # Create a workout
        Workout.objects.create(
            user=self.user,
            title='First Workout',
            date=date.today(),
            duration=30
        )

        badges = check_and_award_badges(self.user)

        self.assertEqual(len(badges), 1)
        self.assertEqual(badges[0].badge_type, 'first_workout')

    def test_10_workouts_badge_awarded(self):
        """Test 10 workouts badge is awarded"""
        from workouts.models import Workout
        from .badge_utils import check_and_award_badges

        # Create 10 workouts
        for i in range(10):
            Workout.objects.create(
                user=self.user,
                title=f'Workout {i}',
                date=date.today() - timedelta(days=i),
                duration=30
            )

        badges = check_and_award_badges(self.user)

        # Should have first_workout and 10_workouts badges
        badge_types = [b.badge_type for b in badges]
        self.assertIn('first_workout', badge_types)
        self.assertIn('10_workouts', badge_types)

    def test_first_goal_badge_awarded(self):
        """Test first goal badge is awarded when goal completed"""
        from .badge_utils import check_and_award_badges

        # Create and complete a goal
        goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            current_number=100,
            unit='km',
            target_date=date.today(),
            is_completed=True,
            completed_date=date.today()
        )

        badges = check_and_award_badges(self.user)

        badge_types = [b.badge_type for b in badges]
        self.assertIn('first_goal', badge_types)

    def test_custom_exercise_badge_awarded(self):
        """Test custom exercise badge is awarded"""
        from workouts.models import Exercise
        from .badge_utils import check_and_award_badges

        # Create a custom exercise
        Exercise.objects.create(
            name='My Custom Exercise',
            category='strength',
            created_by=self.user,
            is_custom=True
        )

        badges = check_and_award_badges(self.user)

        badge_types = [b.badge_type for b in badges]
        self.assertIn('custom_exercise', badge_types)

    def test_7_day_streak_badge_awarded(self):
        """Test 7-day streak badge is awarded"""
        from workouts.models import Workout
        from .badge_utils import check_and_award_badges

        # Create 7 consecutive daily workouts
        for i in range(7):
            Workout.objects.create(
                user=self.user,
                title=f'Workout {i}',
                date=date.today() - timedelta(days=i),
                duration=30
            )

        badges = check_and_award_badges(self.user)

        badge_types = [b.badge_type for b in badges]
        self.assertIn('7_day_streak', badge_types)

    def test_badges_not_awarded_twice(self):
        """Test badges are not awarded multiple times"""
        from workouts.models import Workout
        from .badge_utils import check_and_award_badges

        # Create a workout
        Workout.objects.create(
            user=self.user,
            title='First Workout',
            date=date.today(),
            duration=30
        )

        # Award badges first time
        badges1 = check_and_award_badges(self.user)
        self.assertEqual(len(badges1), 1)

        # Try to award again
        badges2 = check_and_award_badges(self.user)
        self.assertEqual(len(badges2), 0)

    def test_calculate_current_streak(self):
        """Test workout streak calculation"""
        from workouts.models import Workout
        from .badge_utils import calculate_current_streak

        # Create consecutive workouts
        for i in range(5):
            Workout.objects.create(
                user=self.user,
                title=f'Workout {i}',
                date=date.today() - timedelta(days=i),
                duration=30
            )

        streak = calculate_current_streak(self.user)
        self.assertEqual(streak, 5)

    def test_calculate_current_streak_with_gap(self):
        """Test streak calculation with gap in workouts"""
        from workouts.models import Workout
        from .badge_utils import calculate_current_streak

        # Create recent workouts
        for i in range(3):
            Workout.objects.create(
                user=self.user,
                title=f'Recent {i}',
                date=date.today() - timedelta(days=i),
                duration=30
            )

        # Gap of 2 days

        # Old workout
        Workout.objects.create(
            user=self.user,
            title='Old Workout',
            date=date.today() - timedelta(days=6),
            duration=30
        )

        streak = calculate_current_streak(self.user)
        self.assertEqual(streak, 3)


class GoalProgressTests(TestCase):
    """Test cases for goal progress tracking"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_goal_progress_percentage(self):
        """Test goal progress percentage calculation"""
        goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            category='endurance',
            target_number=100,
            current_number=50,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        progress = goal.progress_percentage
        self.assertEqual(progress, 50)

    def test_goal_progress_zero(self):
        """Test goal with zero progress"""
        goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            category='endurance',
            target_number=100,
            current_number=0,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        progress = goal.progress_percentage
        self.assertEqual(progress, 0)

    def test_goal_progress_over_100(self):
        """Test goal progress over 100%"""
        goal = Goal.objects.create(
            user=self.user,
            title='Run 100km',
            category='endurance',
            target_number=100,
            current_number=150,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        progress = goal.progress_percentage
        self.assertEqual(progress, 100)


class GoalDeleteTests(TestCase):
    """Test cases for deleting goals"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

    def test_delete_goal(self):
        """Test deleting a goal"""
        self.client.login(username='testuser', password='testpass123')

        goal_id = self.goal.pk
        response = self.client.post(reverse('goal_delete', args=[self.goal.pk]))

        # Should redirect
        self.assertEqual(response.status_code, 302)

        # Goal should be deleted
        self.assertFalse(Goal.objects.filter(pk=goal_id).exists())

    def test_user_cannot_delete_other_users_goal(self):
        """Test users can't delete goals they don't own"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )

        self.client.login(username='otheruser', password='testpass123')

        response = self.client.post(reverse('goal_delete', args=[self.goal.pk]))

        # Should get 404
        self.assertEqual(response.status_code, 404)

        # Goal should still exist
        self.assertTrue(Goal.objects.filter(pk=self.goal.pk).exists())

