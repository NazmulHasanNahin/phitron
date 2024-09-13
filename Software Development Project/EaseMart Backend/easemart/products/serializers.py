# products/serializers.py
from rest_framework import serializers
from .models import Product
from categories.models import Category

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'original_price', 'discounted_price', 'image', 'product_id', 'category', 'seller')
