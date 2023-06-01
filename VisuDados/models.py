from django.db import models

# Create your models here.

class Data(models.Model):
    dado = models.FloatField()
    dado2 = models.FloatField()
    label = models.FloatField()

    def __str__(self):
        return f"{self.label}"