from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    Non-admins can only view objects.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff

class IsAdminOrOwner(BasePermission):
    """
    Custom permission to only allow admins or owners of an object to view/edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Allow admin users to view/edit any object
        if request.user.is_staff:
            return True

        # Allow authenticated non-admin users to view/edit their own user object
        return obj == request.user

class RolePermission(BasePermission):
    """
    Custom permission based on user roles.
    """
    def has_permission(self, request, view):
        role = getattr(request.user, 'role', None)
        if not role:
            return False

        role_name = role.name
        if role_name == 'Admin':
            return True
        elif role_name == 'Manager':
            return True
        elif role_name == 'Team Lead':
            return True
        elif role_name == 'Team Member':
            return True
        return False

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', None) and request.user.role.name == 'Admin'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', None) and request.user.role.name == 'Manager'

class IsTeamLead(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', None) and request.user.role.name == 'Team Lead'

class IsTeamMember(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user, 'role', None) and request.user.role.name == 'Team Member'
