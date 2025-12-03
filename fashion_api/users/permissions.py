from rest_framework import permissions

# General permissions for all models
class GeneralPermissions(permissions.BasePermission):
    
    """
    Admins => create, update, delete
    Junior_Admins => create, update
    Others => Read
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Must be authenticated for anything else
        if not request.user.is_authenticated:
            return False
        
        # Only allow DELETE for admins
        if request.method == 'DELETE' and request.user.role != 'admin':
            return False
        
        # Allow POST for admin and junior-admin
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user.role in ['admin', 'junior_admin']
        
        return False