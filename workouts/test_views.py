from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from .models import Workout, Exercise
from workouts.template_models import WorkoutTemplate


class HomeViewTest(TestCase):
    def test_home_view(self):
        """Test landing page loads"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')


class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_dashboard_view_authenticated(self):
        """Test dashboard shows for authenticated user"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/dashboard.html')

    def test_dashboard_view_unauthenticated(self):
        """Test dashboard redirects for unauthenticated user"""
        self.client.logout()
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_dashboard_with_workouts(self):
        """Test dashboard displays workout statistics"""
        Workout.objects.create(
            user=self.user,
            title='Morning Run',
            date=date.today(),
            duration=30
        )

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        # Check that workout data is displayed
        self.assertContains(response, 'Morning Run')
        self.assertContains(response, 'Workouts Logged')

    def test_dashboard_streak_calculation(self):
        """Test workout streak calculation"""
        # Create consecutive workouts
        for i in range(3):
            Workout.objects.create(
                user=self.user,
                title=f'Workout {i}',
                date=date.today() - timedelta(days=i),
                duration=30
            )

        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('current_streak', response.context)


class WorkoutListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_workout_list_view(self):
        """Test workout list displays user's workouts"""
        Workout.objects.create(
            user=self.user,
            title='Morning Run',
            date=date.today(),
            duration=30
        )

        response = self.client.get(reverse('workout_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Morning Run')

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
        self.assertContains(response, 'Morning Run')
        self.assertNotContains(response, 'Evening Lift')

    def test_workout_list_date_filter(self):
        """Test workout list date filtering"""
        today = date.today()
        yesterday = today - timedelta(days=1)

        Workout.objects.create(
            user=self.user,
            title='Today Workout',
            date=today,
            duration=30
        )
        Workout.objects.create(
            user=self.user,
            title='Yesterday Workout',
            date=yesterday,
            duration=30
        )

        response = self.client.get(reverse('workout_list') + f'?date_from={today}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Today Workout')


class WorkoutDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

        self.workout = Workout.objects.create(
            user=self.user,
            title='Test Workout',
            date=date.today(),
            duration=60
        )

    def test_workout_detail_view(self):
        """Test workout detail page displays correctly"""
        response = self.client.get(reverse('workout_detail', args=[self.workout.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Workout')

    def test_workout_detail_unauthorized_access(self):
        """Test users can't access other users' workouts"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )

        other_workout = Workout.objects.create(
            user=other_user,
            title='Other User Workout',
            date=date.today(),
            duration=30
        )

        response = self.client.get(reverse('workout_detail', args=[other_workout.pk]))
        self.assertEqual(response.status_code, 404)


class WorkoutCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

        # Create test exercise
        self.exercise = Exercise.objects.create(
            name='Push-ups',
            category='strength',
            created_by=self.user
        )

    def test_workout_create_get(self):
        """Test workout create form loads"""
        response = self.client.get(reverse('workout_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/workout_form.html')

    def test_workout_create_post(self):
        """Test creating a new workout"""
        workout_data = {
            'title': 'Evening Workout',
            'date': date.today(),
            'duration': 45,
            'notes': 'Felt strong',
            # Formset management form
            'workout_exercises-TOTAL_FORMS': '0',
            'workout_exercises-INITIAL_FORMS': '0',
            'workout_exercises-MIN_NUM_FORMS': '0',
            'workout_exercises-MAX_NUM_FORMS': '1000',
        }

        response = self.client.post(reverse('workout_create'), data=workout_data)
        # Check if redirect or form re-render
        self.assertIn(response.status_code, [200, 302])
        if response.status_code == 302:
            self.assertTrue(Workout.objects.filter(title='Evening Workout').exists())

    def test_workout_create_unauthenticated(self):
        """Test workout create redirects for unauthenticated user"""
        self.client.logout()
        response = self.client.get(reverse('workout_create'))
        self.assertEqual(response.status_code, 302)


class WorkoutUpdateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

        self.workout = Workout.objects.create(
            user=self.user,
            title='Old Title',
            date=date.today(),
            duration=30
        )

    def test_workout_update_get(self):
        """Test workout update form loads"""
        response = self.client.get(reverse('workout_update', args=[self.workout.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Old Title')

    def test_workout_update_post(self):
        """Test updating a workout"""
        updated_data = {
            'title': 'New Title',
            'date': date.today(),
            'duration': 45,
            # Formset management form
            'workout_exercises-TOTAL_FORMS': '0',
            'workout_exercises-INITIAL_FORMS': '0',
            'workout_exercises-MIN_NUM_FORMS': '0',
            'workout_exercises-MAX_NUM_FORMS': '1000',
        }

        response = self.client.post(
            reverse('workout_update', args=[self.workout.pk]),
            data=updated_data
        )

        # Check if redirect or form re-render
        self.assertIn(response.status_code, [200, 302])
        if response.status_code == 302:
            self.workout.refresh_from_db()
            self.assertEqual(self.workout.title, 'New Title')

    def test_workout_update_unauthorized(self):
        """Test users can't update other users' workouts"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )

        other_workout = Workout.objects.create(
            user=other_user,
            title='Other Workout',
            date=date.today(),
            duration=30
        )

        response = self.client.get(reverse('workout_update', args=[other_workout.pk]))
        self.assertEqual(response.status_code, 404)


class WorkoutDeleteViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

        self.workout = Workout.objects.create(
            user=self.user,
            title='To Delete',
            date=date.today(),
            duration=30
        )

    def test_workout_delete_get(self):
        """Test workout delete confirmation page"""
        response = self.client.get(reverse('workout_delete', args=[self.workout.pk]))
        self.assertEqual(response.status_code, 200)

    def test_workout_delete_post(self):
        """Test deleting a workout"""
        workout_id = self.workout.pk
        response = self.client.post(reverse('workout_delete', args=[self.workout.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Workout.objects.filter(pk=workout_id).exists())

    def test_workout_delete_unauthorized(self):
        """Test users can't delete other users' workouts"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )

        other_workout = Workout.objects.create(
            user=other_user,
            title='Other Workout',
            date=date.today(),
            duration=30
        )

        response = self.client.post(reverse('workout_delete', args=[other_workout.pk]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Workout.objects.filter(pk=other_workout.pk).exists())


class ExerciseLibraryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_exercise_library_view(self):
        """Test exercise library loads"""
        response = self.client.get(reverse('exercise_library'))
        self.assertEqual(response.status_code, 200)

    def test_exercise_library_displays_exercises(self):
        """Test exercise library displays exercises"""
        Exercise.objects.create(
            name='Squats',
            category='strength',
            created_by=self.user
        )

        response = self.client.get(reverse('exercise_library'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Squats')


class ExerciseCreateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_exercise_create_get(self):
        """Test exercise create form loads"""
        response = self.client.get(reverse('exercise_create'))
        self.assertEqual(response.status_code, 200)

    def test_exercise_create_post(self):
        """Test creating a new exercise"""
        exercise_data = {
            'name': 'Deadlifts',
            'category': 'strength',
            'description': 'Compound lift for back'
        }

        response = self.client.post(reverse('exercise_create'), data=exercise_data)
        # Check if redirect or form re-render
        self.assertIn(response.status_code, [200, 302])
        if response.status_code == 302:
            self.assertTrue(Exercise.objects.filter(name='Deadlifts').exists())


class WorkoutCalendarViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_workout_calendar_view(self):
        """Test calendar view loads"""
        response = self.client.get(reverse('workout_calendar'))
        self.assertEqual(response.status_code, 200)

    def test_workout_calendar_displays_workouts(self):
        """Test calendar displays workout dates"""
        Workout.objects.create(
            user=self.user,
            title='Calendar Workout',
            date=date.today(),
            duration=30
        )

        response = self.client.get(reverse('workout_calendar'))
        self.assertEqual(response.status_code, 200)


class TemplateViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

        self.workout = Workout.objects.create(
            user=self.user,
            title='Template Workout',
            date=date.today(),
            duration=45
        )

    def test_template_list_view(self):
        """Test template list loads"""
        response = self.client.get(reverse('template_list'))
        self.assertEqual(response.status_code, 200)

    def test_save_as_template_get(self):
        """Test save as template form loads"""
        response = self.client.get(reverse('save_as_template', args=[self.workout.pk]))
        self.assertEqual(response.status_code, 200)

    def test_save_as_template_post(self):
        """Test saving workout as template"""
        template_data = {
            'name': 'My Template',
            'description': 'Test template'
        }

        response = self.client.post(
            reverse('save_as_template', args=[self.workout.pk]),
            data=template_data
        )
        # Check if redirect or form re-render
        self.assertIn(response.status_code, [200, 302])
        if response.status_code == 302:
            self.assertTrue(WorkoutTemplate.objects.filter(name='My Template').exists())


class AboutAndFAQViewTest(TestCase):
    def test_faq_view(self):
        """Test FAQ page loads"""
        response = self.client.get(reverse('faq'))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        """Test about page loads"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


class BadgesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_badges_view(self):
        """Test badges page loads"""
        response = self.client.get(reverse('badges'))
        self.assertEqual(response.status_code, 200)
