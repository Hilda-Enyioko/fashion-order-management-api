from django.db.models.signals import pre_save
from .models import Order
from django.dispatch import receiver

@receiver(pre_save, sender=Order)
def restock_inventory_on_cancel(sender, instance, **kwargs):
    if not instance.pk:
        return
    
    old_instance = Order.objects.get(pk=instance.pk)
    
    if old_instance.order_status != 'canceled' and instance.order_status == 'canceled':
        for order_item in instance.order_items.all():
            restock_quantity = order_item.quantity
            inventory_item = order_item.inventory_item
            
            inventory_item.quantity += restock_quantity
            inventory_item._updated_by = instance.updated_by
            inventory_item._change_type = "restocked"
            inventory_item.save(update_fields=["quantity"])