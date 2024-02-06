from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BmiMeasurement(models.Model):
    # STATUS_CHOICES = (
    #     ("underweight", "UNDERWEIGHT"), 
    #     ("normal", "NORMAL"), 
    #     ("overweight", "OVERWEIGHT"), 
    #     ("obese", "OBESE")
    #     )
    # name = models.CharField(max_length=255)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField(null=True)
    message = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)
