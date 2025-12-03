from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from .models import Customer
from users.models import User
from .serializers import CustomerSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """
    Customer viewset with:
    - no creation allowed directly
    - update allowed for admin & junior-admin
    - delete allowed only for admin
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'customer_id'

    def create(self, request, *args, **kwargs):
        # Block direct customer creation
        raise PermissionDenied(detail="Customers cannot be created directly. They are created automatically when an order is made.")
