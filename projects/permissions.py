from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Admin' or request.method in SAFE_METHODS

class IsManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name in ['Admin', 'Manager'] or request.method in SAFE_METHODS

class IsTeamLeadOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name in ['Admin', 'Manager', 'TeamLead'] or request.method in SAFE_METHODS

class IsTeamMemberOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name in ['Admin', 'Manager', 'TeamLead', 'TeamMember'] or request.method in SAFE_METHODS
