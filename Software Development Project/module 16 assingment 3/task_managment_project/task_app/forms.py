from django import forms
from task_app.models import Task
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"
        widgets = {
            'task_assigned_dt': forms.DateInput(attrs={'type': 'date'}),
        }
        
