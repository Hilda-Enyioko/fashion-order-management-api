from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import InventoryItem, InventoryChange

@receiver(pre_save, sender=InventoryItem)
def log_inventory_update(sender, instance, **kwargs):
    if not instance.pk:
        return

    old = InventoryItem.objects.get(pk=instance.pk)

    if old.quantity != instance.quantity:
        InventoryChange.objects.create(
            inventory_item=instance,
            updated_by=getattr(instance, "_changed_by", None),
            old_quantity=old.quantity,
            new_quantity=instance.quantity,
            change_type=getattr(instance, "_change_type", "manual"),
        )


@receiver(post_save, sender=InventoryItem)
def log_inventory_create(sender, instance, created, **kwargs):
    if created:
        InventoryChange.objects.create(
            inventory_item=instance,
            updated_by=getattr(instance, "_changed_by", None),
            old_quantity=0,
            new_quantity=instance.quantity,
            change_type="created",
        )
