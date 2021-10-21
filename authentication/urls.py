from django.urls import path
from .views import UserCreateView, UserListView, UserLoginView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('login/', obtain_auth_token),
    path('register/', UserCreateView.as_view()),
    path('users/', UserListView.as_view()),

]
