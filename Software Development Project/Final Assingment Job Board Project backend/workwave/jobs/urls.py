from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, JobCategoryViewSet, JobSearchView, JobCreateView, JobDetailView
from django.conf import settings
from django.conf.urls.static import static

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('jobs', JobViewSet, basename='job')
router.register('categories', JobCategoryViewSet, basename='job-category')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', JobSearchView.as_view(), name='job-search'),  # Search jobs
    path('jobs/create/', JobCreateView.as_view(), name='create-job'),  # Create a new job
    path('jobs/<int:pk>', JobDetailView.as_view(), name='job-detail'),  # Job detail view
]