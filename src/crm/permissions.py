from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.permissions import SAFE_METHODS


class CanManageClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.team == "1":
            return True
        return False
    def has_object_permission(self, request, view, obj):
        print(request.method)
        if request.user.team == "1":
            return True
        elif request.method in SAFE_METHODS:
            return True
        elif request.method == "PATCH":
            if request.user == obj.client_manager:
                return True
        return False