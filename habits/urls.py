from django.urls import path
from .views import HabitCreateView, HabitListView


urlpatterns = [
    path('', HabitListView.as_view()),
    path('add/', HabitCreateView.as_view()),

]
