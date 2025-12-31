from django import forms
from .models import Goal


class GoalForm(forms.ModelForm):
    """Form for creating and updating goals"""

    class Meta:
        model = Goal
        fields = ['title', 'description', 'category', 'target_number', 'unit', 'current_number', 'target_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Run 100km this month'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Add any notes or details about your goal...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'target_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '100',
                'step': '0.01',
                'min': '0'
            }),
            'current_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'step': '0.01',
                'min': '0'
            }),
            'unit': forms.Select(attrs={
                'class': 'form-select'
            }),
            'target_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'title': 'Goal Title',
            'description': 'Description (Optional)',
            'category': 'Category',
            'target_number': 'Target Value',
            'current_number': 'Current Progress',
            'unit': 'Unit',
            'target_date': 'Target Date',
        }
