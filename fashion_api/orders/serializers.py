from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    image = serializers.PrimaryKeyRelatedField(read_only=True, allow_null=True)

    class Meta:
        model = Order
        fields = '__all__'
        