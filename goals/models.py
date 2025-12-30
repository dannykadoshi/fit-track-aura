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
    ]
    
    UNIT_CHOICES = [
        ('km', 'Kilometers'),
        ('miles', 'Miles'),
        ('kg', 'Kilograms'),
        ('lbs', 'Pounds'),
        ('workouts', 'Workouts'),
        ('days', 'Days'),
        ('hours', 'Hours'),
        ('minutes', 'Minutes'),
        ('reps', 'Repetitions'),
        ('sets', 'Sets'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='custom')
    
    # New fields (with defaults for migration)
    target_number = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Target number (e.g., 100)")
    current_number = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Current progress number")
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default='workouts', help_text="Unit of measurement")
    
    # Old fields (keep for backward compatibility during migration)
    target_value = models.CharField(max_length=100, blank=True, help_text="e.g., '100km', '20 workouts', '5kg'")
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
    
    @property
    def progress_percentage(self):
        """Calculate progress percentage using new number fields"""
        try:
            if self.target_number > 0:
                percentage = (float(self.current_number) / float(self.target_number)) * 100
                return min(int(percentage), 100)  # Cap at 100%
            return 0
        except (ValueError, ZeroDivisionError, AttributeError):
            return 0
    
    @property
    def display_target(self):
        """Display target with unit"""
        return f"{self.target_number} {self.get_unit_display()}"
    
    @property
    def display_current(self):
        """Display current with unit"""
        return f"{self.current_number} {self.get_unit_display()}"
    
    @property
    def target_display(self):
        """Display just the number without decimals if it's a whole number"""
        num = self.target_number
        return int(num) if num == int(num) else num
    
    @property
    def current_display(self):
        """Display just the number without decimals if it's a whole number"""
        num = self.current_number
        return int(num) if num == int(num) else num


class Badge(models.Model):
    """
    Achievement badges that users can earn
    """
    BADGE_TYPES = [
        ('first_workout', '🎯 First Step'),
        ('10_workouts', '💪 Getting Strong'),
        ('7_day_streak', '�� On Fire'),
        ('first_goal', '⭐ Goal Crusher'),
        ('custom_exercise', '✨ Innovator'),
        ('50_workouts', '🚀 Dedicated'),
        ('30_day_streak', '👑 Champion'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='badges')
    badge_type = models.CharField(max_length=20, choices=BADGE_TYPES)
    earned_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'badge_type']
        ordering = ['-earned_date']
    
    def __str__(self):
        return f"{self.get_badge_type_display()} - {self.user.username}"
    
    @property
    def badge_icon(self):
        """Return the emoji icon for this badge"""
        icons = {
            'first_workout': '🎯',
            '10_workouts': '💪',
            '7_day_streak': '🔥',
            'first_goal': '⭐',
            'custom_exercise': '✨',
            '50_workouts': '🚀',
            '30_day_streak': '👑',
        }
        return icons.get(self.badge_type, '🏆')
    
    @property
    def badge_name(self):
        """Return the name without emoji"""
        names = {
            'first_workout': 'First Step',
            '10_workouts': 'Getting Strong',
            '7_day_streak': 'On Fire',
            'first_goal': 'Goal Crusher',
            'custom_exercise': 'Innovator',
            '50_workouts': 'Dedicated',
            '30_day_streak': 'Champion',
        }
        return names.get(self.badge_type, 'Achievement')
    
    @property
    def badge_description(self):
        """Return description of how to earn this badge"""
        descriptions = {
            'first_workout': 'Complete your first workout',
            '10_workouts': 'Log 10 workouts',
            '7_day_streak': 'Maintain a 7-day workout streak',
            'first_goal': 'Complete your first goal',
            'custom_exercise': 'Create a custom exercise',
            '50_workouts': 'Log 50 workouts',
            '30_day_streak': 'Maintain a 30-day workout streak',
        }
        return descriptions.get(self.badge_type, 'Complete a challenge')
