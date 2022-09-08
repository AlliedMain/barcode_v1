from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from . forms import OrderForm, CustomerForm, ProductForm
from .stock_filter import OrderFilter
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from account.decorator import unauthenticated_user

#-------------------(DETAIL/LIST VIEWS) -------------------

def dashBoard(request):
    orders = Order.objects.all().order_by('-order_status')[0:5]
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = Order.objects.all().count()
    delivered = Order.objects.filter(order_status='Delivered').count()
    pending = Order.objects.filter(order_status='Pending').count()



    context = {'customers':customers, 'orders':orders,
    'total_customers':total_customers,'total_orders':total_orders,
    'delivered':delivered, 'pending':pending}
    return render(request, 'inventory/dashBoard.html', context)




#@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'inventory/products.html', context)





@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def customer(request):
    customers = Customer.objects.all
    context = {'customers':customers}
    return render(request, 'inventory/customer.html', context)




    orderFilter = OrderFilter(request.GET, queryset=orders)
    orders = orderFilter.qs

    context = {'customer':customer, 'orders':orders, 'total_orders':total_orders,
    'filter':orderFilter}
    return render(request, 'inventory/customer.html', context)


#-------------------(CREATE VIEWS) -------------------

@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def createOrder(request ):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        else:
            messages.info(request, 'Something wrong')

    context =  {'form':form}
    return render(request, 'inventory/order_form.html', context)

@login_required(login_url='login')
def createproduct(request):
    form = ProductForm()
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.info(request, 'Something Wrong')
    context =  {'form':form}
    return render(request, 'inventory/productOrder.html', context)

#-------------------(UPDATE VIEWS) -------------------

#@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    action = 'update'
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/customer/' + str(order.customer.id))

    context =  {'action':action, 'form':form}
    return render(request, 'inventory/order_form.html', context)

#-------------------(DELETE VIEWS) -------------------

#@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        customer_id = order.customer.id
        customer_url = '/customer/' + str(customer_id)
        order.delete()
        return redirect(customer_url)

    return render(request, 'inventory/delete_item.html', {'item':order})
