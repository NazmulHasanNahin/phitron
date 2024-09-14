# dashboard/urls.py
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('customer/purchases/', CustomerPurchaseListView.as_view(),
         name='customer-purchases'),
    path('customer/cart/', CartView.as_view(), name='cart-items'),
    path('seller/products/', SellerProductListView.as_view(),
         name='seller-products'),
    path('seller/products/<int:pk>/',
         SellerProductDetailView.as_view(), name='seller-product-detail'),
    path('profile/customer/', CustomerProfileUpdateView.as_view(),
         name='customer-profile-update'),
    path('profile/seller/', SellerProfileUpdateView.as_view(),
         name='seller-profile-update'),
]
