from django.contrib import admin
from .models import UserAccount

# Customizing the admin display for UserAccount
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user','account_type')  # Show these fields in admin

# Register the model and custom admin
admin.site.register(UserAccount, UserAccountAdmin)
