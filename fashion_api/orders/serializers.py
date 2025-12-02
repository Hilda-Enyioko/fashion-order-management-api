from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    measurement = serializers.PrimaryKeyRelatedField(read_only=True)
    image = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'