from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.permissions import SAFE_METHODS
from .api_utilities import get_client, get_contract, get_event


class CanManageClient(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.team == "1":
            return True
        elif request.method == "PATCH":
            obj = get_client(id=request.parser_context["kwargs"]["pk"])
            return self.has_object_permission(request, view, obj)
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.client_manager:
            return True
        return False


class CanManageContract(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.team == "1":
            return True
        elif request.method == "PATCH":
            obj = get_contract(id=request.parser_context["kwargs"]["pk"])
            return self.has_object_permission(request, view, obj)
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.client.client_manager:
                return True
        return False

class CanManageEvent(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.team == "1":
            return True
        elif request.method == "PATCH":
            obj = get_event(id=request.parser_context["kwargs"]["pk"])
            return self.has_object_permission(request, view, obj)
        return False

    def has_object_permission(self, request, view, obj):
        if request.user == obj.contract.client.client_manager or request.user == obj.support_manager:
            return True
        return False