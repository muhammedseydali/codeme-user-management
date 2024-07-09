from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at', 'assigned_to')
    list_filter = ('created_at', 'updated_at', 'assigned_to')
    search_fields = ('name', 'description')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'assigned_to')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapse this section by default
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

