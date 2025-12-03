from rest_framework import viewsets, permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission:
    - Admin can delete or update
    - Junior admin can update only
    - Everyone else can read
    """

    def has_permission(self, request, view):

        # NO direct POST for customers
        if request.method == 'POST':
            return False

        # Allow PUT/PATCH for admin and junior-admin
        if request.method in ['PUT', 'PATCH']:
            return request.user.role in ['admin', 'junior_admin']

        return False
