from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from products.models import Product, Purchase, Cart
from .serializers import ProductSerializer, PurchaseSerializer, CartSerializer, CustomerProfileSerializer, SellerProfileSerializer

class CustomerPurchaseListView(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Ensure the user has an associated UserAccount instance and is a customer
        if not hasattr(user, 'useraccount') or user.useraccount.account_type != 'customer':
            raise PermissionDenied("You must be logged in as a customer to view this page.")
        
        # Query purchases associated with the customer
        return Purchase.objects.filter(customer=user.useraccount)


class CartView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Ensure the user has an associated UserAccount instance and is a customer
        if not hasattr(user, 'useraccount') or user.useraccount.account_type != 'customer':
            raise PermissionDenied("You must be logged in as a customer to view this page.")
        
        # Query the cart associated with the customer
        return Cart.objects.filter(user=user.useraccount)


class SellerProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Ensure user is a seller and query using the UserAccount instance
        if not hasattr(user, 'useraccount') or user.useraccount.account_type != 'seller':
            raise PermissionDenied("You must be logged in as a seller to view this page.")
        return Product.objects.filter(seller=user.useraccount)  # Use user.useraccount

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.useraccount)  # Save with user.useraccount



class SellerProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Ensure user is a seller and query using the UserAccount instance
        if not hasattr(user, 'useraccount') or user.useraccount.account_type != 'seller':
            raise PermissionDenied("You must be a seller to view products.")
        return Product.objects.filter(seller=user.useraccount)  # Use user.useraccount



class CustomerProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        # Access account_type from the related UserAccount model
        if not hasattr(user, 'useraccount') or user.useraccount.account_type != 'customer':
            raise PermissionDenied("You must be logged in as a customer to view or update your profile.")
        return user


class SellerProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = SellerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        # Access account_type from the related UserAccount model
        if not hasattr(user, 'useraccount') or user.useraccount.account_type != 'seller':
            raise PermissionDenied("You must be logged in as a seller to view or update your profile.")
        return user
