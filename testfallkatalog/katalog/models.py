from django.db import models

# Create your models here.

class Testfall(models.Model):
    dateiname = models.CharField(max_length=50)
    beschreibung = models.CharField(max_length=200)
    snippet = models.CharField(max_length=100, default="")


