from django.db import models

# Create your models here.


class Habits(models.Model):
    name = models.CharField(max_length=32)
    # author = models.CharField(max)


# class User(models.Model):
#
