from task_app.views import *
from django.urls import path

urlpatterns = [
    path("task_add/",task_add,name="task_add"),
    path('task_show/', show_tasks, name='task_show'),
    path("edit/<int:id>/",edit_task,name="edit_task"),
    path("delete/<int:id>/",delete_task,name="delete_task"),
    path('complete/<int:id>/', complete_task, name='complete_task'),
]
