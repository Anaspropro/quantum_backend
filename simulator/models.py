from django.contrib.auth.models import User
from django.db import models

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class SimulationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    circuit_data = models.JSONField()
    result_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
