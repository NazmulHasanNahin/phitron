from rest_framework import serializers
from patient.models import *

# patient model


class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Patient
        fields = "__all__"
