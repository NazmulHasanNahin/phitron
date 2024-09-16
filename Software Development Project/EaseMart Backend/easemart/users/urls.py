from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import *

router = DefaultRouter()
router.register('user-accounts',UserAcountViewset)
router.register('users',UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationApiView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('activate/<uid64>/<token>/',activate, name='activate'),
]
