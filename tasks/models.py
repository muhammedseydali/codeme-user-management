from django.db import models
from projects.models import Project
from users.models import CustomUser

class Task(models.Model):
    STATUS_CHOICES = [
        ('To-Do', 'To-Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To-Do')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_tasks')

    class Meta:
        db_table = 'report'
        verbose_name = ('report')
        verbose_name_plural = ('report')

    def __str__(self):
        return self.name 