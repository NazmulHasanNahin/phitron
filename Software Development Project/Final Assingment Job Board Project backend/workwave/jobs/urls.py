from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, JobCategoryViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('jobs', JobViewSet, basename='job')
router.register('categories', JobCategoryViewSet, basename='job-category')

urlpatterns = [
    path('', include(router.urls)),
]
