from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employers/', include('employers.urls')),
    path('job_seekers/', include('job_seekers.urls')),
    path('jobs/', include('jobs.urls')),
    path('applications/', include('applications.urls')),
]
