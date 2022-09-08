from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['tags']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
