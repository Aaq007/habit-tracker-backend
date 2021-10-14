from django.shortcuts import render
from rest_framework import generics

from .models import Habit
from .serializers import HabitSerialzer
# Create your views here.


class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerialzer
