# products/models.py
from django.db import models
from django.conf import settings
from categories.models import Category
from users.models import UserAccount

class Purchase(models.Model):
    customer = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.user.username} - {self.product.name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    product_id = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    seller = models.ForeignKey(UserAccount, on_delete=models.CASCADE) #, related_name='products'

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    image = models.URLField()
    
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"
    
    
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return f"{self.product.name} ({self.quantity}) in Purchase {self.purchase.id}"
