from django import forms
from .models import Goal


class GoalForm(forms.ModelForm):
    """Form for creating/editing goals"""

    class Meta:
        model = Goal
        fields = ['title', 'description', 'category', 'target_value', 'current_value', 'target_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Run 100km this month'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe your goal...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'target_value': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 100km, 20 workouts, 5kg'
            }),
            'current_value': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 0km, 0 workouts, 0kg'
            }),
            'target_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
