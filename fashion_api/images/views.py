from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from .models import Image
from .serializers import ImageSerializer
from users.permissions import GeneralPermissions

# Create your views here.
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [GeneralPermissions]
    
    def perform_create(self, serializer):
        # Prevent create action if image is not associated with an order
        order = serializer.validated_data.get('order')
        
        if not order:
            raise ValidationError("An Image must be associated with an order.")
        
        # Prevent create action if image size exceeds 5MB
        image_file = serializer.validate_data.get('image_file')
        max_size = 5 * 1024 * 1024
        
        if image_file.size > max_size:
            raise ValidationError("Image size must not exceed 5MB.")
        
        serializer.save(uploaded_by=self.request.user)