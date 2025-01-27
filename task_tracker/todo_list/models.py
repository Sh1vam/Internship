from django.db import models
from django.utils import timezone

# Task Model with reference to Title and publication date
class Task(models.Model):
    title_text = models.CharField(max_length=100)
    task_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    status_text = models.CharField(max_length=15)
    priority_text = models.CharField(max_length=10)
    deadline_date = models.DateTimeField("deadline date", default=timezone.now)

    def __str__(self):
        return f'{self.task_text} {self.pub_date} {self.status_text} {self.priority_text} {self.deadline_date}'
