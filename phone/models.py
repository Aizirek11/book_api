from django.db import models


class Phone(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)  # ← исправлено
    year = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.brand} {self.model}"

# Create your models here.
