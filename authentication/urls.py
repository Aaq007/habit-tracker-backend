from django.urls import path
from .views import UserCreateView, UserLoginView
urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('create/', UserCreateView.as_view()),
]
