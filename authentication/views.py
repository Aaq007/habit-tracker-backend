from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User
from .serializers import UserCreateSerializer, UserListSerializer, UserLoginSerializer
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (permissions.IsAdminUser,)
    authentication_classes = [TokenAuthentication]
