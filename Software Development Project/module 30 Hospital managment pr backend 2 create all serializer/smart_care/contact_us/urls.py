from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contact_us.views import *



router = DefaultRouter()
router.register('contact_us',Contactusviewset)
urlpatterns = [
    path("",include(router.urls)),
    
]
