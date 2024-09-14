from rest_framework import serializers
from categories.models import Category
from users.models import User
from .models import Cart, Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    seller = serializers.SlugRelatedField(queryset=User.objects.filter(role='seller'), slug_field='username')
    
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'original_price', 'discounted_price', 'image', 'product_id', 'category', 'seller')

    def update(self, instance, validated_data):
        if 'image' not in validated_data:
            validated_data['image'] = instance.image

        return super().update(instance, validated_data)

class CartSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all())

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'quantity']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)