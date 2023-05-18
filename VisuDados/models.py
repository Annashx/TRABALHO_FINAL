from django.db import models

# Create your models here.

class Data(models.Model):
    dado = models.FloatField()
    label = models.IntegerField()

    def __str__(self):
        return f"{self.label}"