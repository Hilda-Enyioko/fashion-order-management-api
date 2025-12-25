from rest_framework import serializers
from .models import InventoryItem

class InventoryItemSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'quantity', 'price', 'category', 'created_at', 'updated_at', 'images']
