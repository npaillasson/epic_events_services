from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class CanAddCollaborators(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.team == "1":
            return True
        else:
            return False


class CanChangeCollaborators(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.team == "1":
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.team == "1":
            return True
        else:
            return False
