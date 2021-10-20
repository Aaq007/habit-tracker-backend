from datetime import datetime
from django.db import models
from authentication.models import User
# Create your models here.


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    date = models.DateTimeField(default=datetime.now)
