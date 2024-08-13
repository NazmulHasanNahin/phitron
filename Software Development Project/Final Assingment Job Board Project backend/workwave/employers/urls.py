from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.contrib.auth import views as auth_views


router = DefaultRouter()
router.register('profiles', EmployerProfileViewSet, basename='employer-profile')
urlpatterns = [
    path('register/', EmployerRegistrationView.as_view(), name='employer-register'),
    path('login/', EmployerLoginView.as_view(), name='employer-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', EmployerDashboardView.as_view(), name='employer-dashboard'),
    path('', include(router.urls)),
    path('applications/', EmployerApplicationsView.as_view(), name='employer-applications'),
    path('profile/<int:pk>/', EmployerProfileDetailView.as_view(), name='employer-profile-detail'),
    path('profile/<int:pk>/edit/', EmployerProfileUpdateView.as_view(), name='employer-profile-update'),
]
