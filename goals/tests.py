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