from django.contrib import admin
from .models import Task
# TaskAdmin: Admin for the Task model
class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title_text","task_text",'priority_text','status_text',]}),
        ("Date information", {"fields": ["pub_date",'deadline_date'], "classes": ["collapse"]}),
        
    ]
    list_display = ["title_text","task_text",'priority_text','status_text','deadline_date']
    search_fields = ["title_text","task_text"]
    list_filter = ["priority_text","deadline_date","status_text","pub_date"]

admin.site.register(Task, TaskAdmin)
# Use double underscore to reference title_text from the related Title model