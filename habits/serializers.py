from datetime import datetime
from rest_framework import serializers
from .models import Habit


class HabitSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name', 'user',  'date']


class HabitCreateSerializer(serializers.Serializer):

    name = serializers.CharField()
    date = serializers.DateTimeField()

    def validate_date(self, value):
        if value is not None:
            datetime.fromisoformat(value)

    def create(self, validated_data):
        user = self.context['reuqest'].user
        habit = Habit.objects.create_user(user=user, **validated_data)
        return habit
