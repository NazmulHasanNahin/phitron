# products/admin.py
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'original_price', 'discounted_price', 'image', 'product_id', 'category', 'seller')

admin.site.register(Product, ProductAdmin)
