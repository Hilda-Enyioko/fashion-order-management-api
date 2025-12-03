from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import Customer
from .serializers import CustomerSerializer
from .permissions import CustomerPermissions
from users.permissions import GeneralPermissions

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [GeneralPermissions, CustomerPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']