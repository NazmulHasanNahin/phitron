from django.db import models
from django.contrib.auth.models import User
from book_app.models import *


#acounts er models.py eta

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    balance=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    
    def __str__(self):
        return self.user.username


class BorrowingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_date = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'