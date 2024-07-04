from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView,LogoutView
from user_app.forms import *
# Create your views here.


def user_singup(rq):
    if rq.method=="POST":
        singup_form=SingUpForm(rq.POST)
        if singup_form.is_valid():
            singup_form.save()
            messages.success(rq,"Your Account have Created Successfully!!!")
            return redirect("login")
    else:
        singup_form=SingUpForm()
    return render(rq,"singup.html",{"form": singup_form,"type":"Singup"})
            
            
class UserLoginView(LoginView):
    template_name="singup.html"
    def get_success_url(self):
        return reverse_lazy("homepage")
    
    def form_valid(self, form):
        messages.success(self.request,"Login Succesfull")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,"Login Unsuccesfull")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["type"]="Login"
        return context
    
def logoutView(rq):
    logout(rq)
    return redirect('login')


@login_required
def edit_profile_view(rq):
    if rq.method == 'POST':
        form = UserProfileForm(rq.POST, instance=rq.user)
        if form.is_valid():
            form.save()
            return redirect('edit-profile')
    else:
        form = UserProfileForm(instance=rq.user)
    return render(rq, 'edit_profile.html', {'form': form})



