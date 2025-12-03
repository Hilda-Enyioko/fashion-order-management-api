from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Measurement
from .serializers import MeasurementSerializer
from users.permissions import GeneralPermissions

# Create your views here.
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all
    serializer_class = MeasurementSerializer
    permission_classes = [GeneralPermissions]
    
    def perform_create(self, serializer):
        # Prevent create if measurement is not associated with an order
        order = serializer.validated_data.get('order')
        
        if not order:
            raise ValidationError("An Image must be associated with an order.")
        
        # Prevent create if measurement is not associated with a customer
        customer = serializer.validated_data.get('customer')
        
        if not customer:
            raise ValidationError("An Image must be associated with a customer.")