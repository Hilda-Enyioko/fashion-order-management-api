from rest_framework import permissions

class IsAdminOrJuniorUploadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Admins can upload and delete
    - Junior admins can upload only
    - No updates allowed
    """
    
    def has_permission(self, request, view):
        
        # Allow read-only for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Must be authenticated for anything else
        if not request.user.is_authenticated:
            return False
        
        # Allow DELETE only for admins
        if request.method == 'DELETE':
            return request.user.role == 'admin'
        
        # Allow POST for admin and junior-admin
        if request.method == 'POST':
            return request.user.role in ['admin', 'junior_admin']
        
        if request.method in ['PUT', 'PATCH']:
            return False