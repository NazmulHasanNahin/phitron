from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appointment.views import *

#   urls   this is Appointment section 


router = DefaultRouter()
router.register('',AppointmentViewset)
urlpatterns = [
    path("",include(router.urls)),
    
]
