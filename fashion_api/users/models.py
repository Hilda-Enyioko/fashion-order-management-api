from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('junior_admin', 'Junior Admin'),
    ]
    
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='junior_admin')
    
    def __str__(self):
        return self.username