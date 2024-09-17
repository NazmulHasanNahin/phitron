# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cart/', CartView.as_view(), name='cart-list-create'),
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),  # Add to cart URL with product_id
    path('cart/remove/<int:cart_item_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),  # Remove from cart URL with cart_item_id
    path('purchase/', PurchaseView.as_view(), name='purchase'),
]
