from django.db import models
from customers.models import Customer
from  users.models import User
from size.models import Size

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]
    
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    payment_status = models.BooleanField(default=False)
    delivery_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_orders')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_orders')
    
    # Add size field
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"Order {self.order_id} - {self.order_status}"