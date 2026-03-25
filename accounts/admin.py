# Open: accounts/admin.py
# DELETE everything
from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'preferred_language', 'credits', 'created_at']
    list_filter = ['preferred_language', 'created_at']
    search_fields = ['user__username', 'user__email']

