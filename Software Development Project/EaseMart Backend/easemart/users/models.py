from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CUSTOMER = 'customer'
    SELLER = 'seller'

    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)
    
    def __str__(self):
        return self.username

    @property
    def is_customer(self):
        return self.role == self.CUSTOMER

    @property
    def is_seller(self):
        return self.role == self.SELLER
