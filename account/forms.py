from django.forms import ModelForm
from .models import Student, Partner, Teacher
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class PartnerForm(ModelForm):
    class Meta:
        model = Partner
        fields = '__all__'
