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
        """Display target with unit - show integers when possible"""
        num = self.target_number
        if num == int(num):
            return f"{int(num)} {self.get_unit_display()}"
        return f"{num} {self.get_unit_display()}"
    
    @property
    def display_current(self):
        """Display current with unit - show integers when possible"""
        num = self.current_number
        if num == int(num):
            return f"{int(num)} {self.get_unit_display()}"
        return f"{num} {self.get_unit_display()}"
    
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
