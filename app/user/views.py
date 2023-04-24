from rest_framework import generics

from user.serializers import UserSerializer
from django.contrib.auth import get_user_model


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
