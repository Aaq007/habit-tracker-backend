from django.urls import path
from .views import HabitCreateView, HabitListView, HabitUpdateView


urlpatterns = [
    path('', HabitListView.as_view()),
    path('create/', HabitCreateView.as_view()),
    path('<int:pk>/', HabitUpdateView.as_view()),
]
