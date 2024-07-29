from django.db import models
from patient.models import *
from doctor.models import *

# Create your models here. appointment


APPOINTMENT_STATUS = [
    ("Completed", "Completed"),
    ("Pending", "Pending"),
    ("Running", "Running"),
]

APPOINTMENT_TYPES = [
    ("Offline", "Offline"),
    ("Online", "Online"),
]


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_types = models.CharField(
        choices=APPOINTMENT_TYPES, max_length=50)
    appointment_status = models.CharField(
        choices=APPOINTMENT_STATUS, max_length=50, default="Pending")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor: {self.doctor.user.first_name} Patient: {self.patient.user.first_name} "
