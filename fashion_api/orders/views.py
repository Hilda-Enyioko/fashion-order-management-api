from django.shortcuts import render
from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializer
from .permissions import OrderPermissions
from users.permissions import GeneralPermissions

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [GeneralPermissions]
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
