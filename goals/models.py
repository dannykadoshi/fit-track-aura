from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Goal(models.Model):
    """
    User fitness goals
    """
    CATEGORY_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('strength', 'Strength'),
        ('endurance', 'Endurance'),
        ('flexibility', 'Flexibility'),
        ('custom', 'Custom'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='custom')
    target_value = models.CharField(max_length=100, help_text="e.g., '100km', '20 workouts', '5kg'")
    current_value = models.CharField(max_length=100, blank=True, default='0')
    target_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def mark_complete(self):
        """Mark goal as completed"""
        self.is_completed = True
        self.completed_date = timezone.now().date()
        self.save()