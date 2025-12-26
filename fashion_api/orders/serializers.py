# orders/serializers.py
from rest_framework import serializers
from .models import Order, OrderItem
from inventory.models import InventoryItem
from size.models import Size

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['inventory_item', 'size', 'quantity', 'total_price']
        read_only_fields = ['total_price']

    def validate(self, attrs):
        item = attrs['inventory_item']
        qty = attrs['quantity']
        if qty <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        if item.quantity < qty:
            raise serializers.ValidationError(f"Not enough stock for {item.name}.")
        return attrs

    def create(self, validated_data):
        item = validated_data['inventory_item']
        qty = validated_data['quantity']

        item.quantity -= qty
        item._changed_by = self.context['request'].user
        item._change_type = "sold"
        item.save(update_fields=['quantity'])

        return OrderItem.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        item = instance.inventory_item
        old_qty = instance.quantity
        new_qty = validated_data.get('quantity', old_qty)
        diff = new_qty - old_qty
        
        item._changed_by = self.context['request'].user
        item._change_type = "sold"


        if diff > 0:
            if item.quantity < diff:
                raise serializers.ValidationError(f"Not enough stock for {item.name}.")
            item.quantity -= diff
        elif diff < 0:
            item.quantity += abs(diff)
        item.save(update_fields=['quantity'])

        instance.quantity = new_qty
        instance.size = validated_data.get('size', instance.size)
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    computed_total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['order_id', 'customer', 'order_status', 'payment_status',
                  'delivery_date', 'created_at', 'updated_at', 'created_by', 
                  'updated_by', 'order_items', 'computed_total_price']

    def create(self, validated_data):
        items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
