from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctor.views import *

# service section urls 

router = DefaultRouter()
router.register('list',Doctorviewset)
router.register('specialization',Specializationviewset)
router.register('designation',Designationviewset)
router.register('available_time',AvailableTimeviewset)
router.register('review',Reviewviewset)
urlpatterns = [
    path("",include(router.urls)),
]
