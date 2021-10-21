from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .serializers import HabitCreateSerializer, HabitSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class HabitCreateView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer
    permission_classes = (IsAuthenticated,)


class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthorOrReadOnly]


class HabitUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthorOrReadOnly]
