from django.shortcuts import render,redirect,get_object_or_404
from task_app.forms import TaskForm
from task_app.models import *

# Create your views here.



def task_add(rq):
    if rq.method == "POST":
        form=TaskForm(rq.POST)
        if form.is_valid():
            form.save()
            return redirect("task_add")
    else:
        form = TaskForm()
    return render(rq,'task_add.html', {'form': form})


def show_tasks(rq):
    tasks = Task.objects.prefetch_related('category').all()
    return render(rq, 'show_task.html', {'tasks': tasks})

# def edit_task(rq, id):
#     tasks = get_object_or_404(Task, pk=id)
#     if rq.method == 'POST':
#         form = TaskForm(rq.POST, instance=tasks)
#         if form.is_valid():
#             form.save()
#             return redirect('task_show')
#     else:
#         form = TaskForm()
#     return render(rq, 'task_add.html', {'form' : form})




def edit_task(rq, id):
    task = get_object_or_404(Task, pk=id)
    if rq.method == 'POST':
        form = TaskForm(rq.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_show')
    else:
        form = TaskForm(instance=task)
    return render(rq, 'task_add.html', {'form': form})



def delete_task(rq, id):
    task = get_object_or_404(Task, pk=id)
    if rq.method == 'POST':
        task.delete()
        return redirect('task_show')
    return render(rq, 'delete_task.html',{'form' : task})


def complete_task(rq, id):
    task = get_object_or_404(Task, pk=id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks')