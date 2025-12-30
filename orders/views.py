from django.shortcuts import render
from rest_framework import viewsets

from .models import Order, OrderItem
from .serializers import OrderSerializer
from .permissions import OrderPermissions
from users.permissions import GeneralPermissions
from drf_spectacular.utils import extend_schema

# Create your views here.

@extend_schema(tags=['Order'])
class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [GeneralPermissions]
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

@extend_schema(tags=['OrderItem'])
class OrderItemViewSet(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [GeneralPermissions]
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)