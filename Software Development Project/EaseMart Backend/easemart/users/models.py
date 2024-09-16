from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPE = (('seller', 'seller'), ('customer', 'customer'),)

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_no = models.CharField(max_length=12)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
