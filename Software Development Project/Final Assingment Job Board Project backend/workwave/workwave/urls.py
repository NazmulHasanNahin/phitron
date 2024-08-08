from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employers/', include('employers.urls')),
    path('job_seekers/', include('job_seekers.urls')),
    path('jobs/', include('jobs.urls')),
    path('applications/', include('applications.urls')),
]