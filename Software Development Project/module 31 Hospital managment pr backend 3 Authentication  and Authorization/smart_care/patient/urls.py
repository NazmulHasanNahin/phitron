from django.urls import path, include
from rest_framework.routers import DefaultRouter
from patient.views import *

# service section urls 

router = DefaultRouter()
router.register('list',Patientviewset)
urlpatterns = [
    path("",include(router.urls)),
    path("register/",UserRegistrationAPIView.as_view(),name="Register"),
    
]
