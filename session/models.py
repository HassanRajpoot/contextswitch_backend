from django.db import models
from django.contrib.auth import get_user_model
from task.models import Task
User = get_user_model()
# Create your models here.
class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    switch_reason = models.CharField(max_length=50, null=True)
