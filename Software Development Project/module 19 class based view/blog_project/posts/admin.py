from django.contrib import admin
from posts.models import *
# Register your models here.

admin.site.register(Posts)
admin.site.register(Comment)