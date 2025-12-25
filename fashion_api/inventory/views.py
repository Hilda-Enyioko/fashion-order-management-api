# inventory/views.py
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from users.permissions import GeneralPermissions

class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    Inventory view:
    - Readable by anyone
    - Editable only by staff/admin
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [GeneralPermissions]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = {
        'category': ['exact'],
        'price': ['gte', 'lte'],
        'quantity': ['lte'],  # low stock
    }
    ordering_fields = ['name', 'quantity', 'price', 'created_at']
    ordering = ['name']
    search_fields = ['name', 'description']
