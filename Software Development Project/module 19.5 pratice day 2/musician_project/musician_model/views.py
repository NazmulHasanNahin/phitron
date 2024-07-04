from django.shortcuts import render,redirect
from musician_model.models import *
from musician_model.forms import *
from django.contrib.auth import logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView,LogoutView

# Create your views here.

def musician_list(rq):
    musicians=Musician.objects.all()
    return render(rq,"musician_list.html",{'musicians': musicians,'user': rq.user})

@login_required
def musician_create(rq):
    if rq.method == "POST":
        form=MusicianForm(rq.POST)
        if form.is_valid():
            form.save()
            return redirect("musician_list")
    else:
        form = MusicianForm()
    return render(rq,'musician_form.html', {'form': form})


# def musician_update(rq,id):
#     musician=Musician.objects.get(pk=id)
#     if rq.method=="POST":
#         form = MusicianForm(rq.POST, instance=musician)
#         if form.is_valid():
#             form.save()
#             return redirect('musician_list')
#     else:
#         form = MusicianForm(instance=musician)
#     return render(rq, 'musician_form.html', {'form': form})



@method_decorator(login_required,name="dispatch")
class musician_update(UpdateView):
    model=Musician
    form_class=MusicianForm
    template_name="musician_form.html"
    pk_url_kwarg= "id"
    success_url=reverse_lazy("musician_list")

@login_required
def musician_delete(rq, id):
    musician = Musician.objects.get(pk=id)
    if rq.method == 'POST':
        musician.delete()
        return redirect('musician_list')
    return render(rq, 'musician_confirm_delete.html', {'musician': musician})

def singup(rq):
    if rq.method=="POST":
        singup_form=SingUpForm(rq.POST)
        if singup_form.is_valid():
            singup_form.save()
            messages.success(rq,"Your Account have Created Successfully!!!")
            return redirect("login")
    else:
        singup_form=SingUpForm()
    return render(rq,"singup.html",{"form": singup_form,"type":"Singup"})

#class based view

class UserLoginView(LoginView):
    template_name="singup.html"
    def get_success_url(self):
        return reverse_lazy("album_list")
    
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

    