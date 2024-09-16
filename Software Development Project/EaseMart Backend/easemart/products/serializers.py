from rest_framework import serializers
from categories.models import Category
from users.models import UserAccount
from .models import Cart, Product

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    
    # Updated to filter based on UserAccount with 'account_type' as 'seller'
    seller = serializers.SlugRelatedField(queryset=UserAccount.objects.filter(account_type='seller'), slug_field='user__username')
    
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
