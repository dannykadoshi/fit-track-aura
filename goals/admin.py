from django.contrib import admin
from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'target_date', 'is_completed']
    list_filter = ['category', 'is_completed', 'target_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'target_date'
    actions = ['mark_as_complete']

    def mark_as_complete(self, request, queryset):
        for goal in queryset:
            goal.mark_complete()
        self.message_user(request, f"{queryset.count()} goal(s) marked as complete.")
    mark_as_complete.short_description = "Mark selected goals as complete"
