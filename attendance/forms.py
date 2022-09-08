from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *



class AttendanceForm(ModelForm):
    class Meta:
        model = LoginLogoutLog
        fields = '__all__'
