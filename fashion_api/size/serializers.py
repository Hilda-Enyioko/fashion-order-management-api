from rest_framework import serializers
from .models import Size

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ["id", "uk_size", "bust", "waist", "hips"]
        
        read_only_fields = fields