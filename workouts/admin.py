from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_custom', 'created_by']
    list_filter = ['category', 'is_custom']
    search_fields = ['name']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date', 'duration', 'created_at']
    list_filter = ['date', 'user']
    search_fields = ['title', 'notes']
    inlines = [WorkoutExerciseInline]
    date_hierarchy = 'date'


@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ['exercise', 'workout', 'sets', 'reps', 'weight', 'unit']
    list_filter = ['exercise', 'workout__user']