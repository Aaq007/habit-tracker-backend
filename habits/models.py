from django.db import models

# Create your models here.


class Habits(models.Model):
    name = models.CharField()
    author = models.CharField()


# class User(models.Model):
#
