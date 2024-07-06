from django.db import models
from django.contrib.auth.models import User
from accounts.constants import *
# Create your models here.



class UserBankAccount(models.Model):
    user = models.OneToOneField(
        User, related_name="account", on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    initial_deposit_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)


class UserAdress(models.Model):
    user = models.OneToOneField(
        User, related_name="adress", on_delete=models.CASCADE)
    street_adress = models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    postal_code=models.IntegerField(max_length=4)
    contry=models.CharField(max_length=20)
    
