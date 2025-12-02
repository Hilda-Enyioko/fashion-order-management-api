from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Admin can delete or update
    - Junior admin can update only
    - Everyone else can read
    """

    def has_permission(self, request, view):
        # Allow read-only requests for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Must be authenticated for anything else
        if not request.user.is_authenticated:
            return False

        # Only allow DELETE for admins
        if request.method == 'DELETE' and request.user.role != 'admin':
            return False

        # NO direct POST for customers
        if request.method == 'POST':
            return False

        # Allow PUT/PATCH for admin and junior-admin
        if request.method in ['PUT', 'PATCH']:
            return request.user.role in ['admin', 'junior_admin']

        return False
