from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, AdminUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .models import User
from .permissions import CanAddCollaborators, CanChangeCollaborators


class UserCreate(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CanAddCollaborators]
    serializer_class = AdminUserSerializer

    def perform_create(self, serializer):
            user = User.objects.create_user(
                email=serializer.validated_data["email"],
                first_name=serializer.validated_data["first_name"],
                last_name=serializer.validated_data["last_name"],
                team=serializer.validated_data["team"],
            )
            user.set_password(serializer.validated_data["password"])
            user.save()

class DisplayUser(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CanChangeCollaborators]
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        if request.user.team == "1":
            serializer = AdminUserSerializer(queryset, many=True)
        else:
            serializer = UserSerializer(queryset, many=True)
        print(serializer.__dict__)
        return Response(serializer.data)
# Create your views here.
