from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contact_us.views import *

# contact us section urls 


router = DefaultRouter()
router.register('',Contactusviewset)
urlpatterns = [
    path("",include(router.urls)),
    
]
