from rest_framework import serializers
from .models import InventoryItem, InventoryChange

class InventoryItemSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    history = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'description', 'quantity', 'price', 'category', 'created_by', 'images', 'history']
        
        read_only_fields = ['created_by', 'images', 'history']
        
        
class InventoryChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryChange
        fields = ['id', 'inventory_item', 'updated_by', 'old_quantity', 'new_quantity', 'change_type', 'timestamp']
        read_only_fields = ['inventory_item', 'updated_by', 'old_quantity', 'new_quantity', 'change_type', 'timestamp']
