from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('jobs', JobViewSet, basename='job')
router.register('categories', JobCategoryViewSet, basename='job-category'),

urlpatterns = [
    path('', include(router.urls)),
    path('search/', JobSearchView.as_view(), name='job-search'), #http://127.0.0.1:8000/jobs/search/?q=developer
]
