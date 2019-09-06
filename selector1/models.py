from django.db import models

class City(models.Model):
    name        = models.CharField(max_length=200)
    latitude    = models.DecimalField(decimal_places=5, max_digits=10)
    longitude   = models.DecimalField(decimal_places=5, max_digits=10)
