from django.shortcuts import render
from rest_framework import generics

from .models import Habit
from .serializers import HabitSerialzer
# Create your views here.


class HabitListView(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerialzer

    def get_object(self):
        return self.request.user


class HabitUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerialzer

    def get_object(self):
        return self.request.user
