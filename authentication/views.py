from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserCreateSerializer, UserLoginSerializer
# Create your views here.


class UserLoginView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def get_object(self):
        return self.request.user


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
