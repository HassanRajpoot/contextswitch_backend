from django.db import models
from django.conf import settings
from task.models import Task

User = settings.AUTH_USER_MODEL

class Session(models.Model):
    SWITCH_REASONS = [
        ("distracted", "Distracted"),
        ("urgent", "Urgent"),
        ("bored", "Bored"),
        ("notification", "Notification"),
        ("energy_drop", "Energy Drop"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    switch_reason = models.CharField(
        max_length=20, choices=SWITCH_REASONS, null=True, blank=True
    )

    def duration(self):
        if self.end_time:
            return (self.end_time - self.start_time).seconds
        return 0

