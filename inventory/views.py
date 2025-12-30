from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import InventoryItem, InventoryChange
from .serializers import InventoryItemSerializer, InventoryChangeSerializer
from users.permissions import GeneralPermissions, ReadOnlyPermissions
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['InventoryItem'])
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [GeneralPermissions]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = {
        "category": ["exact"],
        "price": ["gte", "lte"],
        "quantity": ["lte"],
    }
    ordering_fields = ["name", "quantity", "price", "created_at"]
    ordering = ["name"]
    search_fields = ["name", "description"]

    def perform_create(self, serializer):
        instance = serializer.save(created_by=self.request.user)
        instance._updated_by = self.request.user
        instance._change_type = "created"
        instance.save(update_fields=["quantity"])

    def perform_update(self, serializer):
        instance = serializer.save()
        instance._updated_by = self.request.user
        instance._change_type = "manual"
        instance.save(update_fields=["quantity"])



@extend_schema(tags=['InventoryChange'])
class InventoryChangeViewSet(viewsets.ReadOnlyModelViewSet):
    from .models import InventoryChange
    from .serializers import InventoryChangeSerializer

    queryset = InventoryChange.objects.all().order_by('-timestamp')
    serializer_class = InventoryChangeSerializer
    permission_classes = [ReadOnlyPermissions]