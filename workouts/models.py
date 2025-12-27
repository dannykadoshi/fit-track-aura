from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Exercise(models.Model):
    """
    Exercise library - contains both predefined and user-created exercises
    """
    CATEGORY_CHOICES = [
        ('strength', 'Strength'),
        ('cardio', 'Cardio'),
        ('flexibility', 'Flexibility'),
        ('sports', 'Sports'),
    ]
    
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_custom = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Workout(models.Model):
    """
    Main workout session
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    duration = models.PositiveIntegerField(help_text="Duration in minutes", null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.date}"
    
    def total_exercises(self):
        return self.workout_exercises.count()


class WorkoutExercise(models.Model):
    """
    Individual exercises within a workout (many-to-many through table)
    """
    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('lbs', 'Pounds'),
    ]
    
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workout_exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(null=True, blank=True)
    reps = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default='kg')
    distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, help_text="Distance in km")
    duration = models.PositiveIntegerField(null=True, blank=True, help_text="Duration in minutes")
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.exercise.name} in {self.workout.title}"