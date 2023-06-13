from django.db import models

# Create your models here.

class Data(models.Model):
    temperatura = models.FloatField()
    concentracao = models.FloatField()

    def __str__(self):
        return f"{self.concentracao}"