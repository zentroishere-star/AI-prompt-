# Open: chatbot/admin.py
# DELETE everything


from django.contrib import admin
from .models import Query, Feedback


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['user', 'detected_intent', 'detected_language', 'selected_model', 'created_at']
    list_filter = ['detected_intent', 'detected_language', 'selected_model', 'created_at']
    search_fields = ['user__username', 'original_input']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'title', 'is_approved', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_approved', 'is_featured', 'is_positive', 'created_at']
    search_fields = ['user__username', 'title', 'message']
    readonly_fields = ['created_at', 'updated_at']
    actions = ['approve_feedback', 'mark_as_featured']

    def approve_feedback(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} feedback(s) approved.')

    approve_feedback.short_description = 'Approve selected feedback'

    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} feedback(s) marked as featured.')

    mark_as_featured.short_description = 'Mark as featured'

# SAVE the file