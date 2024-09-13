# products/models.py
from django.db import models
from django.conf import settings

from categories.models import Category  # Make sure to import Category

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    product_id = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
