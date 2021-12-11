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
        if request.user.team == "1":
            return True
        elif request.method in SAFE_METHODS:
            return True
        elif request.method == "PATCH":
            if request.user == obj.client_manager:
                return True
        return False


class CanManageContract(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.team == "1":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.team == "1":
            return True
        elif request.method in SAFE_METHODS:
            return True
        elif request.method == "PATCH":
            if request.user == obj.client.client_manager:
                return True
        return False

class CanManageEvent(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.team == "1":
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.team == "1":
            return True
        elif request.method in SAFE_METHODS:
            return True
        elif request.method == "PATCH":
            if request.user == obj.contract.client.client_manager or request.user == obj.support_manager:
                return True
        return False