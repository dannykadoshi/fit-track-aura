from django.contrib import admin
from .models import Goal, Badge


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'target_date', 'is_completed']
    list_filter = ['category', 'is_completed', 'created_at']
    search_fields = ['title', 'user__username']
    date_hierarchy = 'target_date'


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['badge_type', 'user', 'earned_date']
    list_filter = ['badge_type', 'earned_date']
    search_fields = ['user__username']
    date_hierarchy = 'earned_date'
    readonly_fields = ['earned_date']
