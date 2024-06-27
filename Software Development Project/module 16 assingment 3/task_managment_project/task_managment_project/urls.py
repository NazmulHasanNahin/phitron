
from django.contrib import admin
from django.urls import path,include
from task_managment_project.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="homepage"),
    path("task/",include("task_app.urls")),
    path("category/",include("category_app.urls")),
]
