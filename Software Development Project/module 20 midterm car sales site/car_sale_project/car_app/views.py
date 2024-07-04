from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Car, Brand,Order
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *
from django.utils.decorators import method_decorator





# Create your views here.

def car_list_view(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    selected_brand = request.GET.get('brand')
    if selected_brand:
        cars = cars.filter(brand__name=selected_brand)
    context = {
        'cars': cars,
        'brands': brands,
    }
    return render(request, 'car_list.html', context)


def car_detail_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    comments = car.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('car-detail', pk=car.pk)
    else:
        form = CommentForm()
    return render(request, 'car_detail.html', {'car': car, 'comments': comments, 'form': form})



@login_required
def buy_car_view(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.quantity > 0:
        Order.objects.create(user=request.user, car=car)
        car.quantity -= 1
        car.save()
        return redirect('order-history')
    return redirect('car-detail', pk=pk)



@method_decorator(login_required,name="dispatch")
class AddBrandView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'add_brand.html'
    success_url = reverse_lazy('car-list')
    
@method_decorator(login_required,name="dispatch")    
class AddCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('car-list')
    
@login_required
def order_history_view(rq):
    orders = Order.objects.filter(user=rq.user)
    context = {
        'orders': orders
    }
    return render(rq, 'order_history.html', context)