# categories/serializers.py
from rest_framework import serializers
from .models import Category
from products.serializers import ProductSerializer 
from products.models import Product

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'products')
