from rest_framework import permissions

# General permissions for all models
from rest_framework import permissions

class GeneralPermissions(permissions.BasePermission):
    """
    Admins => create, update, delete
    Junior_Admins => create, update
    Others => Read
    """
    def has_permission(self, request, view):
        # Read-only for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_authenticated:
            return False
        
        # DELETE allowed only for admins
        if request.method == 'DELETE' and getattr(request.user, 'role', '') != 'admin':
            return False
        
        # POST / PUT / PATCH allowed for admins and junior admins
        if request.method in ['POST', 'PUT', 'PATCH']:
            return getattr(request.user, 'role', '') in ['admin', 'junior_admin']
        
        return False
    

class ReadOnlyPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
    
class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read-only permission for SAFE_METHODS
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.role == 'admin'