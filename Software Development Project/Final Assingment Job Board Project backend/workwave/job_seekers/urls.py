from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('profiles', JobSeekerProfileViewSet, basename='jobseeker-profile')

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),  # Login, logout, password reset, etc.
    path('auth/registration/', JobSeekerRegistrationView.as_view(), name='jobseeker-register'),  # Registration
    path('dashboard/', JobSeekerDashboardView.as_view(), name='jobseeker-dashboard'),
    path('', include(router.urls)),
    path('applications/', JobSeekerApplicationsView.as_view(), name='jobseeker-applications'),
    path('profile/', JobSeekerProfileDetailView.as_view(), name='jobseeker-profile-detail'),
    path('profile/edit/', JobSeekerProfileUpdateView.as_view(), name='jobseeker-profile-update'),
]
