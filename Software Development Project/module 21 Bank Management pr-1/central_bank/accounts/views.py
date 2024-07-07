from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from accounts.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login,logout

# Create your views here.


class UserRegistrationView(FormView):
    template_name="accounts/user_registration.html"
    form_class=UserRegistrationForm
    success_url = reverse_lazy("register")
    
    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    
    