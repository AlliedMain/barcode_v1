from django import forms
from django.contrib.auth.models import User
from .models import User_profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class UserForm(UserCreationForm):
    email = forms.EmailField()


    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }

class UserProfileInForm(ModelForm):
    class Meta():
        model = User_profile
        fields ='__all__'
    
