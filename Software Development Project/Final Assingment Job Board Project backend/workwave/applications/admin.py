from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'job_seeker', 'resume', 'date_applied')
    search_fields = ('job__title', 'applicant__username') 
    list_filter = ('job', 'date_applied')

admin.site.register(Application, ApplicationAdmin)