# dashboard/models.py

from django.db import models
from django.conf import settings
from products.models import Product
from users.models import UserAccount


class SellerDashboard(models.Model):
    seller = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    total_sales = models.PositiveIntegerField(default=0)
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Dashboard for {self.seller.username}"

class CustomerDashboard(models.Model):
    customer = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    recent_purchases = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"Dashboard for {self.customer.username}"
