# dashboard/serializers.py
from rest_framework import serializers
from products.models import Product, Purchase,Cart
from users.models import User
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'original_price', 'discounted_price','product_id', 'category', 'image']

class PurchaseSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Purchase
        fields = ['id','purchase_date','customer','product','quantity',]


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']
        
class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']