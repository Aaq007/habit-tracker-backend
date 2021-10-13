from django.db import models

# Create your models here.


class Habit(models.Model):
    name = models.CharField(max_length=32)
    # author = models.CharField(max)
