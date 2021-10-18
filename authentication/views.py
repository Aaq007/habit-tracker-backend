from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserLoginSerializer
# Create your views here.


class UserLoginView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
