from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer, AdminUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .models import User
from .permissions import CanAddCollaborators, CanChangeCollaborators
from .api_utilities import get_user, partial_user_update
from .validators import custom_password_validator


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
        queryset = get_user(user_id="all")
        if request.user.team == "1":
            serializer = AdminUserSerializer(queryset, many=True)
        else:
            serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = get_user(user_id=self.kwargs["pk"])
        if request.user.team == "1":
            serializer = AdminUserSerializer(queryset)
        else:
            serializer = UserSerializer(queryset)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = get_user(user_id=self.kwargs["pk"])
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        self.object = get_user(user_id=self.kwargs["pk"])
        serializer = AdminUserSerializer(self.object, data=request.data, partial=True)


        if serializer.is_valid():
            print(serializer.data)
            partial_user_update(serializer, request.data, self.object)
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def perform_update(self, serializer):
    #    print(serializer)

    #   serializer.save(serializer.data["password"]
    #    custom_password_validator(serializer.validated_data["password"])



    #def update(self, request, *args, **kwargs):
    #    queryset = get_user(user_id=self.kwargs["pk"])
    #    serializer = AdminUserSerializer(queryset, request.data, partial=True)
    #    serializer.is_valid(raise_exception=True)
    #    self.perform_update(serializer)
    #    return Response(serializer.data)


# Create your views here.
