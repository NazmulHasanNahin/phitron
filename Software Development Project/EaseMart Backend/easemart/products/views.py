# products/views.py
from rest_framework import viewsets
from .models import Product
from rest_framework.permissions import AllowAny
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer