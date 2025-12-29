from django.forms import inlineformset_factory
from django import forms
from .models import Workout, WorkoutExercise, Exercise


class WorkoutForm(forms.ModelForm):
    """Form for creating/editing workouts"""
    class Meta:
        model = Workout
        fields = ['title', 'date', 'duration', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Upper Body Strength Training'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '45',
                'min': '1'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'How did you feel? Any observations?'
            }),
        }


class WorkoutExerciseForm(forms.ModelForm):
    """Form for adding exercises to a workout"""
    exercise = forms.ModelChoiceField(
        queryset=Exercise.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'unit', 'distance', 'duration']
        widgets = {
            'sets': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '3',
                'min': '1'
            }),
            'reps': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '10',
                'min': '1'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '50',
                'min': '0',
                'step': '0.5'
            }),
            'unit': forms.Select(attrs={
                'class': 'form-control'
            }),
            'distance': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Distance in km',
                'min': '0',
                'step': '0.1'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duration in minutes',
                'min': '1'
            }),
        }


# Django formsets for handling multiple exercises
WorkoutExerciseFormSet = inlineformset_factory(
    Workout,
    WorkoutExercise,
    form=WorkoutExerciseForm,
    extra=1,  # Show 1 empty form by default
    can_delete=True,
    min_num=0,  # Changed from 1 to 0 - no minimum required
    validate_min=False  # Changed from True to False
)