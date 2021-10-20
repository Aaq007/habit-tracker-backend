from datetime import datetime
from rest_framework import serializers
from .models import Habit


class HabitSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name', 'date']

    def validate_date(self, value):
        if value is not None:
            datetime.fromisoformat(value)
