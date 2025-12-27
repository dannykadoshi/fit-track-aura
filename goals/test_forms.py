from django.test import TestCase
from goals.forms import GoalForm
from datetime import date, timedelta


class GoalFormTest(TestCase):
    """Test cases for GoalForm"""
    
    def test_goal_form_valid_data(self):
        """Test form with valid data"""
        form_data = {
            'title': 'Run 100km',
            'description': 'Build endurance',
            'category': 'endurance',
            'target_value': '100km',
            'current_value': '0km',
            'target_date': date.today() + timedelta(days=30)
        }
        form = GoalForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_goal_form_missing_title(self):
        """Test form without required title"""
        form_data = {
            'category': 'endurance',
            'target_value': '100km',
            'target_date': date.today() + timedelta(days=30)
        }
        form = GoalForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        
    def test_goal_form_missing_target_date(self):
        """Test form without required target date"""
        form_data = {
            'title': 'Run 100km',
            'category': 'endurance',
            'target_value': '100km'
        }
        form = GoalForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('target_date', form.errors)