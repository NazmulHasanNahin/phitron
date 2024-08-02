from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.contrib.auth import views as auth_views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('profiles', EmployerProfileViewSet, basename='employer-profile')
urlpatterns = [
    path('register/', EmployerRegistrationView.as_view(), name='employer-register'),
    path('login/', EmployerLoginView.as_view(), name='employer-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', EmployerDashboardView.as_view(), name='employer-dashboard'),
    path('', include(router.urls)),
]
