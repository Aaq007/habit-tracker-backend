from rest_framework import serializers
from .models import Habit


class HabitSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
