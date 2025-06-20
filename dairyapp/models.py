
from django.db import models

class MilkDelivery(models.Model):
    customer_id = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

class MilkingLog(models.Model):
    milk_time = models.TimeField()
    milk_quantity = models.CharField(max_length=100)

class HealthLog(models.Model):
    health_notes = models.TextField()
