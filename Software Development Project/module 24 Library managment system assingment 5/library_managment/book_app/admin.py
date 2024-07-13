from django.contrib import admin
from .models import Book, Category, Review

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'borrowing_price', 'category')
    search_fields = ('title', 'category__name')
    list_filter = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating')
    search_fields = ('user__username', 'book__title')
    list_filter = ('rating',)
