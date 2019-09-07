from django.db import models
from django.utils import timezone


class MyDate(models.Model):
    mydate = models.DateField(default=timezone.now)
