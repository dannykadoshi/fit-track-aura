from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import Workout
from .pdf_utils import generate_workouts_pdf
from io import BytesIO


class PDFGenerationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
    def test_generate_empty_workouts_pdf(self):
        """Test PDF generation with no workouts"""
        workouts = Workout.objects.filter(user=self.user)
        pdf_buffer = generate_workouts_pdf(workouts, self.user)
        
        self.assertIsInstance(pdf_buffer, BytesIO)
        self.assertGreater(pdf_buffer.getbuffer().nbytes, 0)
        
    def test_generate_workouts_pdf_with_data(self):
        """Test PDF generation with workout data"""
        Workout.objects.create(
            user=self.user,
            title='Morning Run',
            date=date.today(),
            duration=30,
            notes='Great run!'
        )
        Workout.objects.create(
            user=self.user,
            title='Evening Lift',
            date=date.today(),
            duration=45,
            notes='Good session'
        )
        
        workouts = Workout.objects.filter(user=self.user)
        pdf_buffer = generate_workouts_pdf(workouts, self.user)
        
        self.assertIsInstance(pdf_buffer, BytesIO)
        self.assertGreater(pdf_buffer.getbuffer().nbytes, 0)
        
    def test_pdf_buffer_is_readable(self):
        """Test that generated PDF buffer can be read"""
        Workout.objects.create(
            user=self.user,
            title='Test Workout',
            date=date.today(),
            duration=30
        )
        
        workouts = Workout.objects.filter(user=self.user)
        pdf_buffer = generate_workouts_pdf(workouts, self.user)
        
        # Try to read the buffer
        pdf_content = pdf_buffer.getvalue()
        self.assertIsInstance(pdf_content, bytes)
        self.assertGreater(len(pdf_content), 0)
        
        # Check PDF header
        self.assertTrue(pdf_content.startswith(b'%PDF'))
        
    def test_pdf_with_multiple_workouts(self):
        """Test PDF generation with multiple workouts"""
        for i in range(10):
            Workout.objects.create(
                user=self.user,
                title=f'Workout {i}',
                date=date.today(),
                duration=30 + i,
                notes=f'Notes for workout {i}'
            )
        
        workouts = Workout.objects.filter(user=self.user)
        pdf_buffer = generate_workouts_pdf(workouts, self.user)
        
        self.assertIsInstance(pdf_buffer, BytesIO)
        self.assertGreater(pdf_buffer.getbuffer().nbytes, 0)
        
    def test_pdf_with_long_workout_title(self):
        """Test PDF handles long workout titles"""
        Workout.objects.create(
            user=self.user,
            title='A' * 200,  # Very long title
            date=date.today(),
            duration=30
        )
        
        workouts = Workout.objects.filter(user=self.user)
        pdf_buffer = generate_workouts_pdf(workouts, self.user)
        
        self.assertIsInstance(pdf_buffer, BytesIO)
        self.assertGreater(pdf_buffer.getbuffer().nbytes, 0)
        
    def test_pdf_with_special_characters(self):
        """Test PDF handles special characters in workout data"""
        Workout.objects.create(
            user=self.user,
            title='Workout with émojis 💪 & spëcial çhars!',
            date=date.today(),
            duration=30,
            notes='Notes with special chars: © ® ™'
        )
        
        workouts = Workout.objects.filter(user=self.user)
        pdf_buffer = generate_workouts_pdf(workouts, self.user)
        
        self.assertIsInstance(pdf_buffer, BytesIO)
        self.assertGreater(pdf_buffer.getbuffer().nbytes, 0)
