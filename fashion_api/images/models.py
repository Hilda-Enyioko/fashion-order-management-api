from django.db import models
from users.models import User
from inventory.models import InventoryItem

# Create your models here.
class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='order_images/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='uploaded_images')
    deleted_at = models.DateTimeField(auto_now=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='deleted_images')
    
    def __str__(self):
        return f"Image {self.image_id} for Order {self.order.order_id}"