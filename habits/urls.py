from django.urls import path
from .views import HabitListView


urlpatterns = [
    path('habits/', HabitListView.as_view()),
]
