from django.contrib import admin
from contact_us.models import *
# Register your models here. contact us section


class ContactModelAdmin(admin.ModelAdmin):
    list_display=["name","phone","problem"]
admin.site.register(ContactUs,ContactModelAdmin)  
