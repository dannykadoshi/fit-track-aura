"""Additional tests to increase coverage for workouts views"""
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from .models import Workout, Exercise


class WorkoutViewsCoverageTests(TestCase):
    """Test uncovered paths in workouts views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_workout_list_empty(self):
        """Test workout list when no workouts exist"""
        response = self.client.get(reverse('workout_list'))
        self.assertEqual(response.status_code, 200)

    def test_workout_list_unauthenticated(self):
        """Test workout list requires login"""
        self.client.logout()
        response = self.client.get(reverse('workout_list'))
        self.assertEqual(response.status_code, 302)

    def test_workout_detail_unauthenticated(self):
        """Test workout detail requires login"""
        self.client.logout()
        response = self.client.get(reverse('workout_detail', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_workout_create_unauthenticated(self):
        """Test workout create requires login"""
        self.client.logout()
        response = self.client.get(reverse('workout_create'))
        self.assertEqual(response.status_code, 302)

    def test_workout_update_unauthenticated(self):
        """Test workout update requires login"""
        self.client.logout()
        response = self.client.get(reverse('workout_update', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_workout_delete_unauthenticated(self):
        """Test workout delete requires login"""
        self.client.logout()
        response = self.client.get(reverse('workout_delete', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_exercise_library_unauthenticated(self):
        """Test exercise library requires login"""
        self.client.logout()
        response = self.client.get(reverse('exercise_library'))
        self.assertEqual(response.status_code, 302)

    def test_exercise_create_unauthenticated(self):
        """Test exercise create requires login"""
        self.client.logout()
        response = self.client.get(reverse('exercise_create'))
        self.assertEqual(response.status_code, 302)

    def test_workout_detail_nonexistent_404(self):
        """Test accessing nonexistent workout returns 404"""
        response = self.client.get(reverse('workout_detail', args=[99999]))
        self.assertEqual(response.status_code, 404)

    def test_workout_update_nonexistent_404(self):
        """Test updating nonexistent workout returns 404"""
        response = self.client.get(reverse('workout_update', args=[99999]))
        self.assertEqual(response.status_code, 404)

    def test_workout_delete_nonexistent_404(self):
        """Test deleting nonexistent workout returns 404"""
        response = self.client.get(reverse('workout_delete', args=[99999]))
        self.assertEqual(response.status_code, 404)

    def test_exercise_create_invalid_form(self):
        """Test creating exercise with invalid data"""
        invalid_data = {
            'name': '',  # Missing name
            'category': 'invalid',
        }
        response = self.client.post(reverse('exercise_create'), data=invalid_data)
        self.assertEqual(response.status_code, 200)

    def test_workout_detail_other_user_404(self):
        """Test accessing another user's workout returns 404"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='pass123'
        )
        other_workout = Workout.objects.create(
            user=other_user,
            title='Other Workout',
            date=date.today(),
            duration=30
        )

        response = self.client.get(reverse('workout_detail', args=[other_workout.pk]))
        self.assertEqual(response.status_code, 404)

    def test_workout_update_other_user_404(self):
        """Test updating another user's workout returns 404"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='pass123'
        )
        other_workout = Workout.objects.create(
            user=other_user,
            title='Other Workout',
            date=date.today(),
            duration=30
        )

        response = self.client.get(reverse('workout_update', args=[other_workout.pk]))
        self.assertEqual(response.status_code, 404)

    def test_workout_delete_other_user_404(self):
        """Test deleting another user's workout returns 404"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='pass123'
        )
        other_workout = Workout.objects.create(
            user=other_user,
            title='Other Workout',
            date=date.today(),
            duration=30
        )

        response = self.client.post(reverse('workout_delete', args=[other_workout.pk]))
        self.assertEqual(response.status_code, 404)

    def test_dashboard_unauthenticated(self):
        """Test dashboard requires login"""
        self.client.logout()
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_workout_calendar_unauthenticated(self):
        """Test calendar requires login"""
        self.client.logout()
        response = self.client.get(reverse('workout_calendar'))
        self.assertEqual(response.status_code, 302)

    def test_exercise_create_success(self):
        """Test successful exercise creation"""
        exercise_data = {
            'name': 'New Exercise',
            'category': 'strength',
            'description': 'Test'
        }
        response = self.client.post(reverse('exercise_create'), data=exercise_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Exercise.objects.filter(name='New Exercise').exists())

    def test_workout_delete_get(self):
        """Test delete confirmation page"""
        workout = Workout.objects.create(
            user=self.user,
            title='Test Workout',
            date=date.today(),
            duration=30
        )

        response = self.client.get(reverse('workout_delete', args=[workout.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Workout')

    def test_workout_list_search(self):
        """Test workout list search functionality"""
        Workout.objects.create(
            user=self.user,
            title='Morning Run',
            date=date.today(),
            duration=30
        )
        Workout.objects.create(
            user=self.user,
            title='Evening Lift',
            date=date.today(),
            duration=45
        )

        response = self.client.get(reverse('workout_list') + '?search=Run')
        self.assertEqual(response.status_code, 200)

    def test_save_as_template_unauthenticated(self):
        """Test save template requires login"""
        self.client.logout()
        response = self.client.get(reverse('save_as_template', args=[1]))
        self.assertEqual(response.status_code, 302)

    def test_template_list_unauthenticated(self):
        """Test template list requires login"""
        self.client.logout()
        response = self.client.get(reverse('template_list'))
        self.assertEqual(response.status_code, 302)
