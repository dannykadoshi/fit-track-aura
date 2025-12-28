from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Workout, Exercise, WorkoutExercise
from datetime import date


class WorkoutModelTest(TestCase):
    """Test cases for Workout model"""

    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_workout_creation(self):
        """Test that a workout can be created"""
        workout = Workout.objects.create(
            user=self.user,
            title='Test Workout',
            date=date.today(),
            duration=45
        )
        self.assertEqual(workout.title, 'Test Workout')
        self.assertEqual(workout.user, self.user)

    def test_workout_str_method(self):
        """Test the string representation of workout"""
        workout = Workout.objects.create(
            user=self.user,
            title='Morning Run',
            date=date.today()
        )
        expected = f"Morning Run - {date.today()}"
        self.assertEqual(str(workout), expected)


class ExerciseModelTest(TestCase):
    """Test cases for Exercise model"""

    def test_exercise_creation(self):
        """Test that an exercise can be created"""
        exercise = Exercise.objects.create(
            name='Bench Press',
            category='strength'
        )
        self.assertEqual(exercise.name, 'Bench Press')
        self.assertEqual(exercise.category, 'strength')

    def test_exercise_name_is_stored_correctly(self):
        """Test that exercise name is stored correctly"""
        exercise = Exercise.objects.create(name='Squats', category='strength')
        retrieved = Exercise.objects.get(name='Squats')
        self.assertEqual(retrieved.name, 'Squats')
        self.assertEqual(retrieved.category, 'strength')


class WorkoutViewTest(TestCase):
    """Test cases for Workout views"""

    def setUp(self):
        """Set up test client and user"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_workout_list_view_requires_login(self):
        """Test that workout list requires authentication"""
        response = self.client.get(reverse('workout_list'))
        # Should redirect to login
        self.assertEqual(response.status_code, 302)

    def test_workout_list_view_authenticated(self):
        """Test workout list view when logged in"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('workout_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/workout_list.html')

    def test_workout_create_view(self):
        """Test workout creation view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('workout_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/workout_form.html')

    def test_user_can_only_see_own_workouts(self):
        """Test that users can only see their own workouts"""
        # Create workout for test user
        self.client.login(username='testuser', password='testpass123')
        workout1 = Workout.objects.create(
            user=self.user,
            title='My Workout',
            date=date.today()
        )

        # Create another user and their workout
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        workout2 = Workout.objects.create(
            user=other_user,
            title='Other Workout',
            date=date.today()
        )

        # Get workout list
        response = self.client.get(reverse('workout_list'))

        # Should only see own workout
        self.assertContains(response, 'My Workout')
        self.assertNotContains(response, 'Other Workout')


class WorkoutDeleteTest(TestCase):
    """Test cases for Workout deletion"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.workout = Workout.objects.create(
            user=self.user,
            title='Test Workout',
            date=date.today()
        )

    def test_delete_workout_get_request(self):
        """Test delete confirmation page loads"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('workout_delete', args=[self.workout.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/workout_confirm_delete.html')

    def test_delete_workout_post_request(self):
        """Test workout is deleted on POST"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('workout_delete', args=[self.workout.pk])
        )
        # Should redirect after deletion
        self.assertEqual(response.status_code, 302)
        # Workout should be deleted
        self.assertFalse(Workout.objects.filter(pk=self.workout.pk).exists())

    def test_user_cannot_delete_other_users_workout(self):
        """Test users can't delete workouts they don't own"""
        # Create another user
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )

        # Login as other user
        self.client.login(username='otheruser', password='testpass123')

        # Try to delete first user's workout
        response = self.client.post(
            reverse('workout_delete', args=[self.workout.pk])
        )

        # Should get 404 or redirect
        self.assertIn(response.status_code, [302, 404])
        # Workout should still exist
        self.assertTrue(Workout.objects.filter(pk=self.workout.pk).exists())


class WorkoutDetailTest(TestCase):
    """Test cases for Workout detail view"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.exercise = Exercise.objects.create(
            name='Bench Press',
            category='strength'
        )
        self.workout = Workout.objects.create(
            user=self.user,
            title='Upper Body',
            date=date.today(),
            duration=45
        )
        self.workout_exercise = WorkoutExercise.objects.create(
            workout=self.workout,
            exercise=self.exercise,
            sets=3,
            reps=10,
            weight=60,
            unit='kg'
        )

    def test_workout_detail_view(self):
        """Test workout detail page displays correctly"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(
            reverse('workout_detail', args=[self.workout.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Upper Body')
        self.assertContains(response, 'Bench Press')
        self.assertContains(response, '3')  # sets
        self.assertContains(response, '10')  # reps
        self.assertContains(response, '60')  # weight
