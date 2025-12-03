from rest_framework import permissions

class OrderPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        
        # Allow POST, PUT, PATCH, DELETE actions for admin only
        if request.method == ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.role == 'admin'
        
        return False