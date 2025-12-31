from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise
from .template_models import WorkoutTemplate, TemplateExercise


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


class TemplateExerciseInline(admin.TabularInline):
    model = TemplateExercise
    extra = 1


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_custom', 'created_by']
    list_filter = ['category', 'is_custom']
    search_fields = ['name', 'description']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'date', 'duration']
    list_filter = ['date', 'user']
    search_fields = ['title', 'notes']
    inlines = [WorkoutExerciseInline]
    date_hierarchy = 'date'


@admin.register(WorkoutTemplate)
class WorkoutTemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['name', 'description']
    inlines = [TemplateExerciseInline]
    date_hierarchy = 'created_at'
