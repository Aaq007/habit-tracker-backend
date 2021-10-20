from django.shortcuts import render
from rest_framework import generics

from .models import Habit
from .serializers import HabitCreateSerializer, HabitSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class HabitCreateView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer


class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthorOrReadOnly]


class HabitUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthorOrReadOnly]
