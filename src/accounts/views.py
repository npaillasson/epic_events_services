from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .models import User
from .permissions import CanAddCollaborators


class UserCreate(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CanAddCollaborators]
    serializer_class = UserSerializer

    def perform_create(self, serializer):
            user = User.objects.create_user(
                email=serializer.validated_data["email"],
                first_name=serializer.validated_data["first_name"],
                last_name=serializer.validated_data["last_name"],
                team=serializer.validated_data["team"],
            )
            user.set_password(serializer.validated_data["password"])
            user.save()

# Create your views here.
