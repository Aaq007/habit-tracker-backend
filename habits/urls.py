from django.urls import path
from .views import HabitListView, HabitUpdateView


urlpatterns = [
    path('', HabitListView.as_view()),
    path('<int:pk>/', HabitUpdateView.as_view()),
]
