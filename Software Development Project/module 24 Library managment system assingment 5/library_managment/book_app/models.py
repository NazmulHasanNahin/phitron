from django.db import models
from django.contrib.auth.models import User


#book_app er models.py eta

class Category(models.Model):
    name=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="book_images/")
    borrowing_price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="books")
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name="reviews")
    review_text=models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    
    def __str__(self):
        return f'{self.user.username} review on {self.book.title}'
