from django.contrib import admin
from .models import Job, JobCategory

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'date_posted', 'category')
    search_fields = ('title', 'employer__username')
    list_filter = ('category',)


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)