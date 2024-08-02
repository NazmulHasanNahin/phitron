from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
]
