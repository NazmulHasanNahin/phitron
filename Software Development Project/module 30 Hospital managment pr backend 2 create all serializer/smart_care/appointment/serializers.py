from rest_framework import serializers
from appointment.models import *

# this is Appointment section


class AppointmentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
