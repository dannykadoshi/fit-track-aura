"""Additional tests to increase coverage for goals views"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Goal
from datetime import date, timedelta


class GoalViewsCoverageTests(TestCase):
    """Test uncovered paths in goals views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_goal_create_invalid_form(self):
        """Test creating goal with invalid data"""
        invalid_data = {
            'title': '',  # Missing title
            'category': 'invalid_category',
        }
        response = self.client.post(reverse('goal_create'), data=invalid_data)
        # Form should fail validation, page re-renders
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/goal_form.html')

    def test_goal_update_invalid_form(self):
        """Test updating goal with invalid data"""
        goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        invalid_data = {
            'title': '',  # Missing title
            'category': 'strength',
        }
        response = self.client.post(reverse('goal_update', args=[goal.pk]), data=invalid_data)
        # Form should fail validation
        self.assertEqual(response.status_code, 200)

    def test_goal_complete_marks_complete(self):
        """Test that goal_complete marks goal as complete"""
        goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.get(reverse('goal_complete', args=[goal.pk]))
        self.assertEqual(response.status_code, 302)

        goal.refresh_from_db()
        self.assertTrue(goal.is_completed)
        self.assertIsNotNone(goal.completed_date)

    def test_goal_delete_get_confirmation(self):
        """Test delete confirmation page"""
        goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.get(reverse('goal_delete', args=[goal.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/goal_confirm_delete.html')
        self.assertContains(response, 'Test Goal')

    def test_goal_list_with_completed_and_active(self):
        """Test goal list shows both completed and active goals"""
        # Create active goal
        active_goal = Goal.objects.create(
            user=self.user,
            title='Active Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        # Create completed goal
        completed_goal = Goal.objects.create(
            user=self.user,
            title='Completed Goal',
            category='endurance',
            target_number=50,
            unit='km',
            target_date=date.today() - timedelta(days=10),
            is_completed=True,
            completed_date=date.today()
        )

        response = self.client.get(reverse('goal_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Goal')
        self.assertContains(response, 'Completed Goal')

    def test_goal_update_get_form(self):
        """Test update goal GET request shows form with pre-filled data"""
        goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.get(reverse('goal_update', args=[goal.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Goal')

    def test_goal_create_get_form(self):
        """Test create goal GET request shows empty form"""
        response = self.client.get(reverse('goal_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goals/goal_form.html')

    def test_goal_create_success_message(self):
        """Test success message appears after creating goal"""
        goal_data = {
            'title': 'New Goal',
            'category': 'strength',
            'target_number': 100,
            'current_number': 0,
            'unit': 'km',
            'target_date': date.today() + timedelta(days=30)
        }

        response = self.client.post(reverse('goal_create'), data=goal_data, follow=True)
        self.assertContains(response, 'Goal created successfully')

    def test_goal_update_success_message(self):
        """Test success message appears after updating goal"""
        goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        updated_data = {
            'title': 'Updated Goal',
            'category': 'strength',
            'target_number': 150,
            'current_number': 50,
            'unit': 'km',
            'target_date': date.today() + timedelta(days=60)
        }

        response = self.client.post(
            reverse('goal_update', args=[goal.pk]),
            data=updated_data,
            follow=True
        )
        self.assertContains(response, 'Goal updated successfully')

    def test_goal_delete_success_message(self):
        """Test success message appears after deleting goal"""
        goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.post(reverse('goal_delete', args=[goal.pk]), follow=True)
        self.assertContains(response, 'Goal deleted successfully')

    def test_goal_complete_success_message(self):
        """Test success message appears after completing goal"""
        goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.get(reverse('goal_complete', args=[goal.pk]), follow=True)
        self.assertContains(response, 'marked as complete')

    def test_goal_unauthenticated_redirect(self):
        """Test unauthenticated users are redirected"""
        self.client.logout()

        response = self.client.get(reverse('goal_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_goal_update_other_user_404(self):
        """Test updating another user's goal returns 404"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='pass123'
        )
        other_goal = Goal.objects.create(
            user=other_user,
            title='Other Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.get(reverse('goal_update', args=[other_goal.pk]))
        self.assertEqual(response.status_code, 404)

    def test_goal_complete_other_user_404(self):
        """Test completing another user's goal returns 404"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='pass123'
        )
        other_goal = Goal.objects.create(
            user=other_user,
            title='Other Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.get(reverse('goal_complete', args=[other_goal.pk]))
        self.assertEqual(response.status_code, 404)

    def test_goal_delete_get_other_user_404(self):
        """Test deleting another user's goal returns 404"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='pass123'
        )
        other_goal = Goal.objects.create(
            user=other_user,
            title='Other Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.get(reverse('goal_delete', args=[other_goal.pk]))
        self.assertEqual(response.status_code, 404)


class GoalExportTests(TestCase):
    """Test PDF export functionality"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_export_goals_pdf_unauthenticated(self):
        """Test PDF export requires login"""
        self.client.logout()
        response = self.client.get(reverse('export_goals_pdf'))
        self.assertEqual(response.status_code, 302)

    def test_export_goals_pdf_empty(self):
        """Test exporting PDF with no goals"""
        response = self.client.get(reverse('export_goals_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

    def test_export_goals_pdf_with_goals(self):
        """Test exporting PDF with goals"""
        Goal.objects.create(
            user=self.user,
            title='Test Goal',
            category='strength',
            target_number=100,
            unit='km',
            target_date=date.today() + timedelta(days=30)
        )

        response = self.client.get(reverse('export_goals_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
