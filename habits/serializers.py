from datetime import datetime
from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name', 'user',  'date']


class HabitCreateSerializer(serializers.Serializer):

    name = serializers.CharField()
    date = serializers.DateTimeField()

    def validate_date(self, value):
        if value is not None:
            return datetime.fromisoformat(str(value))

    def create(self, validated_data):
        user = self.context['request'].user
        habit = Habit.objects.create(user=user, **validated_data)
        return habit
