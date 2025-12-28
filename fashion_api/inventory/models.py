from django.db import models
from users.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inventory_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'category'], name='unique_inventory_item')
        ]

    def __str__(self):
        return self.name


class InventoryChange(models.Model):
    CHANGE_TYPES = [
        ("created", "Created"),
        ("restocked", "Restocked"),
        ("sold", "Sold"),
        ("manual", "Manual"),
    ]

    inventory_item = models.ForeignKey(
        InventoryItem, on_delete=models.CASCADE, related_name="history"
    )
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    old_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveIntegerField()
    change_type = models.CharField(max_length=20, choices=CHANGE_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.inventory_item}: {self.old_quantity} → {self.new_quantity} ({self.change_type})"
