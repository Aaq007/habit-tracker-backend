from django.shortcuts import render
from rest_framework import generics

from .models import Habit
from .serializers import HabitCreateSerializer, HabitSerializer
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class HabitCreateView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitCreateSerializer


class HabitListView(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_object(self):
        return self.request.user


class HabitUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_object(self):
        return self.request.user
