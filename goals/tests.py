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
