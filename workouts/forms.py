from django import forms
from django.forms import inlineformset_factory
from .models import Workout, WorkoutExercise, Exercise


class WorkoutForm(forms.ModelForm):
    """Form for creating and updating workouts"""
    class Meta:
        model = Workout
        fields = ['title', 'date', 'duration', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Morning Cardio'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minutes'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'How did it go?'}),
        }


class WorkoutExerciseForm(forms.ModelForm):
    """Form for individual exercises within a workout"""
    
    def __init__(self, *args, **kwargs):
        # Get user from kwargs if provided
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user:
            # Get default and custom exercises
            default_exercises = Exercise.objects.filter(is_custom=False).order_by('name')
            custom_exercises = Exercise.objects.filter(created_by=user, is_custom=True).order_by('name')
            
            # Create choices with optgroups
            choices = []
            if default_exercises.exists():
                choices.append(('Default Exercises', [(ex.id, ex.name) for ex in default_exercises]))
            if custom_exercises.exists():
                choices.append(('My Custom Exercises', [(ex.id, f"{ex.name} ✨") for ex in custom_exercises]))
            
            # If no groups, just show all
            if not choices:
                self.fields['exercise'].queryset = Exercise.objects.all()
            else:
                self.fields['exercise'].choices = [('', '---------')] + choices
    
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'unit', 'distance', 'duration', 'notes']
        widgets = {
            'exercise': forms.Select(attrs={'class': 'form-select exercise-select'}),
            'sets': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Sets'}),
            'reps': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Reps'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight', 'step': '0.5'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
            'distance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'km', 'step': '0.1'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minutes'}),
            'notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notes'}),
        }


# Formset for managing multiple exercises in a workout
WorkoutExerciseFormSet = inlineformset_factory(
    Workout,
    WorkoutExercise,
    form=WorkoutExerciseForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True,
)


class ExerciseForm(forms.ModelForm):
    """Form for creating custom exercises"""
    class Meta:
        model = Exercise
        fields = ['name', 'category', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "e.g., Farmer's Walk"
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe the exercise (optional)...'
            }),
        }
        labels = {
            'name': 'Exercise Name',
            'category': 'Category',
            'description': 'Description (Optional)',
        }
