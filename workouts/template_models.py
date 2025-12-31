from django.db import models
from django.contrib.auth.models import User
from .models import Exercise


class WorkoutTemplate(models.Model):
    """
    Reusable workout templates
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_templates')
    name = models.CharField(max_length=200, help_text="Template name (e.g., 'Monday Chest Day')")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'name']

    def __str__(self):
        return f"{self.name} - {self.user.username}"


class TemplateExercise(models.Model):
    """
    Exercises within a workout template
    """
    UNIT_CHOICES = [
        ('kg', 'KG'),
        ('lbs', 'LBS'),
    ]

    template = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField(null=True, blank=True)
    reps = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=3, choices=UNIT_CHOICES, default='kg')
    distance = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.exercise.name} in {self.template.name}"
