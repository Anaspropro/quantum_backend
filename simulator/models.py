from django.db import models

class Circuit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Simulation(models.Model):
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    input_data = models.JSONField()
    output_data = models.JSONField()
    simulated_at = models.DateTimeField(auto_now_add=True)
