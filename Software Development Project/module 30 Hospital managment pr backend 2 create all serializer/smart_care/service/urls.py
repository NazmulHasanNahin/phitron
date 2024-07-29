from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service.views import *

# service section urls 

router = DefaultRouter()
router.register('',Serviceviewset)
urlpatterns = [
    path("",include(router.urls)),
    
]
