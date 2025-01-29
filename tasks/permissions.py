from rest_framework.permissions import BasePermission

class IsTaskOwner(BasePermission):
    """Allow access only to the owner of the task."""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user