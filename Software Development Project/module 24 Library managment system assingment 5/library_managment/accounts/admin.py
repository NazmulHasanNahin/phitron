from django.contrib import admin
from .models import UserProfile, BorrowingHistory

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    search_fields = ('user__username',)

@admin.register(BorrowingHistory)
class BorrowingHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowing_date', 'returned')
    search_fields = ('user__username', 'book__title')
    list_filter = ('returned',)
