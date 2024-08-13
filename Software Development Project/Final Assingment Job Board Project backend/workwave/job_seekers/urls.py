from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('profiles', JobSeekerProfileViewSet,
                basename='jobseeker-profile')

urlpatterns = [
    path('register/', JobSeekerRegistrationView.as_view(),
         name='jobseeker-register'),
    path('login/', JobSeekerLoginView.as_view(), name='jobseeker-login'),
    path('', include(router.urls)),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', JobSeekerDashboardView.as_view(), name='jobseeker-dashboard'),
    path('profile/<int:pk>/', JobSeekerProfileDetailView.as_view(), name='jobseeker-profile-detail'),
    path('profile/<int:pk>/edit/', JobSeekerProfileUpdateView.as_view(), name='job-seeker-profile-update'),
]
