# taskboards/admin.py
from django.contrib import admin
from .models import TaskBoard

@admin.register(TaskBoard)
class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'assigned_to', 'created_at')
    search_fields = ('title', 'status', 'assigned_to__first_name', 'assigned_to__last_name')
    list_filter = ('status', 'assigned_to')
