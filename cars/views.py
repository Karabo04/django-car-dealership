from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only
from django.contrib.auth.models import User
from .models import *

from .forms import SaleForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username {username} already exists')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, f'Account created for {username} - now login')
            return redirect('login')
    
    return render(request, 'cars/register.html')


        


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request, 'cars/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def home(request):
    if not request.user.is_authenticated:
        return redirect('cars')
     
    cars= Car.objects.all()
    customers= Customer.objects.all()
    sales= Sale.objects.all()

    total_cars=cars.count()
    total_customers=customers.count()
    total_sales=sales.count()

    pending = sales.filter(status='pending').count()
    out_for_delivery = sales.filter(status='out_for_delivery').count()
    delivered = sales.filter(status='delivered').count()
    cancelled = sales.filter(status='cancelled').count()

    context = {
        "total_cars": total_cars,
        "total_customers": total_customers,
        "total_sales": total_sales,
        "pending": pending,
        "out_for_delivery": out_for_delivery,
        "delivered": delivered,
        "cancelled": cancelled,
        'sales': sales
    }
    return render(request, 'cars/dashboard.html', context)

def cars(request):
    cars= Car.objects.all()

    query= request.GET.get('q')
    if query:
        cars=cars.filter(Q(brand__icontains=query)| Q(model__icontains=query))

    fuel_type=request.GET.get('fuel_type')
    if fuel_type:
        cars=cars.filter(fuel_type=fuel_type)

    body_type = request.GET.get('body_type')
    if body_type:
        cars = cars.filter(body_type=body_type)

    context={"cars": cars}
    return render(request, 'cars/cars.html', context)

   



@login_required(login_url='login')
def customer(request):
    customers= Customer.objects.all()
    context={"customers": customers}
    return render(request, 'cars/customers.html', context )


@login_required(login_url='login')
def sales(request):
    sales=Sale.objects.all()
    context={"sales": sales}
    return render(request, 'cars/sales.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'salesperson'])
def createSale(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    car_id = request.GET.get('car')  # <-- NEW: get ?car=1 from URL
    
    SaleFormSet = inlineformset_factory(Customer, Sale, fields=('car', 'price', 'date_sold', 'sales_person', 'status'), extra=1)  # extra=1 not 5
    
    # If car_id exists, pre-select it
    if car_id:
        formset = SaleFormSet(queryset=Sale.objects.none(), instance=customer, initial=[{'car': car_id}])
    else:
        formset = SaleFormSet(queryset=Sale.objects.none(), instance=customer)
    
    if request.method == 'POST':
        formset = SaleFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    context = {'formset': formset, 'customer': customer}
    return render(request, 'cars/sale_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'salesperson'])
def updateSale(request, pk):
    sale = get_object_or_404(Sale, id=pk)
    form = SaleForm(instance=sale)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form, 'sale': sale}
    return render(request, 'cars/updatesale_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteSale(request, pk):
    sale= get_object_or_404(Sale, id=pk)
    if request.method =='POST':
        sale.delete()
        return redirect('/')
    context={'item': sale }
    return render(request, 'cars/delete.html', context)  


def car_view(request, pk):
    car= get_object_or_404(Car, id=pk)
    customers = Customer.objects.all()
    return render(request, "cars/car_detail.html", {"car": car, "customers":customers})


@login_required(login_url='login')
def customer_view(request, pk):
    customer= get_object_or_404(Customer, id=pk)
    return render(request, "cars/customer_detail.html", {"customer": customer})