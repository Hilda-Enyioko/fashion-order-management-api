from rest_framework import serializers
from .models import Order
from customers.models import Customer

class OrderSerializer(serializers.ModelSerializer):
    measurement = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)
    image = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)

    class Meta:
        model = Order
        fields = '__all__'
        