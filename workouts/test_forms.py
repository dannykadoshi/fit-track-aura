from django.test import TestCase
from workouts.forms import WorkoutForm, WorkoutExerciseForm
from datetime import date


class WorkoutFormTest(TestCase):
    """Test cases for WorkoutForm"""

    def test_workout_form_valid_data(self):
        """Test form with valid data"""
        form_data = {
            'title': 'Test Workout',
            'date': date.today(),
            'duration': 45,
            'notes': 'Felt great!'
        }
        form = WorkoutForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_workout_form_missing_title(self):
        """Test form without required title"""
        form_data = {
            'date': date.today(),
            'duration': 45
        }
        form = WorkoutForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_workout_form_missing_date(self):
        """Test form without required date"""
        form_data = {
            'title': 'Test Workout',
            'duration': 45
        }
        form = WorkoutForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def test_workout_form_negative_duration(self):
        """Test form with invalid duration"""
        form_data = {
            'title': 'Test Workout',
            'date': date.today(),
            'duration': -10
        }
        form = WorkoutForm(data=form_data)
        self.assertFalse(form.is_valid())


class WorkoutExerciseFormTest(TestCase):
    """Test cases for WorkoutExerciseForm"""

    def test_exercise_form_valid_data(self):
        """Test form with valid exercise data"""
        from workouts.models import Exercise
        exercise = Exercise.objects.create(
            name='Bench Press',
            category='strength'
        )

        form_data = {
            'exercise': exercise.id,
            'sets': 3,
            'reps': 10,
            'weight': 60,
            'unit': 'kg'
        }
        form = WorkoutExerciseForm(data=form_data)
        self.assertTrue(form.is_valid())
