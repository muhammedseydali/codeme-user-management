from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ('name',) 
    list_display = ('name', 'project', 'status', 'assigned_to', 'created_by')
    list_filter = ('status', 'assigned_to', 'created_by')
    search_fields = ('name', 'description')

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'status', 'project', 'assigned_to', 'created_by')
        }),
        ('Date Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('status', 'created_by')


