from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from car_sale_project.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/",include("user_app.urls")),
    path('car/', include('car_app.urls')),
    path('',home,name="homepage"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
