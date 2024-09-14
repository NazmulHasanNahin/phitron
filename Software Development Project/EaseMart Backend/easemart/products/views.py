# products/views.py
from rest_framework import viewsets
from .models import Product, Cart
from rest_framework.permissions import AllowAny
from .serializers import ProductSerializer, CartSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, NotFound, ValidationError
from rest_framework.decorators import api_view, permission_classes


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            raise PermissionDenied("You must be logged in to view cart items.")
        return Cart.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        if not product_id:
            return Response({"detail": "Product ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = Cart.objects.get_or_create(
            user=user, product=product, defaults={'quantity': quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
            return Response({"detail": "Product quantity updated in cart."}, status=status.HTTP_200_OK)

        return Response({"detail": "Product added to cart."}, status=status.HTTP_201_CREATED)


class AddToCartView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product not found.")

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        return Response({
            "message": "Product added to cart successfully!",
            "cart_item": CartSerializer(cart_item).data
        }, status=status.HTTP_201_CREATED)



class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        cart_item_id = self.kwargs.get('cart_item_id')

        try:
            cart_item = Cart.objects.get(id=cart_item_id, user=request.user)
        except Cart.DoesNotExist:
            raise ValidationError("Cart item not found.")

        cart_item.delete()

        return Response({"message": "Item removed from cart successfully!"}, status=status.HTTP_204_NO_CONTENT)