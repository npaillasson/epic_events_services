from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.permissions import SAFE_METHODS

class CanAddCollaborators(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.team)
        if request.user.team == "1":
            return True
        else:
            return False

    def has_object_permissionpermission(self, request, view, obj):
        if request.user.team == "1":
            return True
        else:
            return False