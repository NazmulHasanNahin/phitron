from django.contrib import admin
from catagories.models import Catagory
# Register your models here.

# admin.site.register(Catagory)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("name",) }
    list_display=["name","slug"]
    
    
admin.site.register(Catagory,CategoryAdmin)