from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApplicationListCreateView, ApplicationDetailView, ApplicationViewSet

router = DefaultRouter()
router.register('applications', ApplicationViewSet, basename='application')

urlpatterns = [
    path('apply/', ApplicationListCreateView.as_view(), name='apply-for-job'),
    path('<int:pk>/', ApplicationDetailView.as_view(), name='application-detail'),
    path('', include(router.urls)),
]
