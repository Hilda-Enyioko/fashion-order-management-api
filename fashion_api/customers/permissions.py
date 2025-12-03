from rest_framework import viewsets, permissions

class CustomerPermissions(permissions.BasePermission):

    def has_permission(self, request, view):

        # Allow create and delete actions for admin only
        if request.method in ['POST', 'DELETE']:
            return request.user.role == 'admin'

        # Allow PUT/PATCH for admin and junior-admin
        if request.method in ['PUT', 'PATCH']:
            return request.user.role in ['admin', 'junior_admin']

        return False
