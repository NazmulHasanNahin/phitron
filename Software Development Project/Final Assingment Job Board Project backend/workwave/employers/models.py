from django.db import models
from django.contrib.auth.models import User


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()

    def __str__(self):
        return self.company_name
