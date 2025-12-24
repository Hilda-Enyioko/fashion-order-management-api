from django.db import models

# Create your models here.
class Size(models.Model):
    UK_SIZE_MODELS = [
        (4, "UK 4"),
        (6, "UK 6"),
        (8, "UK 8"),
        (10, "UK 10"),
        (12, "UK 12"),
        (14, "UK 14"),
        (16, "UK 16"),
        (18, "UK 18"),
        (20, "UK 20"),
    ]
    
    uk_size = models.PositiveSmallIntegerField(choices=UK_SIZE_MODELS, unique=True)
    bust = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    hips = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"UK {self.uk_size}"