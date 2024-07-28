from django.contrib import admin
from appointment.models import *
    
# Register your models here. appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display=["doctor_name","patient_name","appointment_types","appointment_status","time","cancel"]
    
    def patient_name(self,obj):
        return obj.patient.user.first_name
    def doctor_name(self,obj):
        return obj.doctor.user.last_name

admin.site.register(Appointment,AppointmentAdmin)
