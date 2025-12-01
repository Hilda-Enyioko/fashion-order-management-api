from django.db import models
from customers.models import Customer
from orders.models import Order
from users.models import User

# Create your models here.
class Measurement(models.Model):
    measurement_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='measurements')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='measurements')
    values = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Measurement {self.measurement_id} for Customer {self.customer.id}"