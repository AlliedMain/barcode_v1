from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from common.forms import UserForm , UserProfileInForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from account.decorator import  unauthenticated_user, admin_only
from account.models import *
from inventory.models import *
from learning_manager.models import *
from django.contrib.auth.models import User
from account.decorator import unauthenticated_user, admin_only

# Create your views here.
@admin_only
def admin_view(request):
    information = Teacher.objects.all()
    student = Student.objects.all()
    product = Product.objects.all()
    order = Order.objects.all()

    return render(request, 'admin/Spela_main_dash.html', context = {'information':information,
                                                                              'student':student,
                                                                              'product':product,
                                                                              'order':order,})

'''def teacher_dash(request):
    student = Student.objects.all()
    subject = Subject.objects.all()
    lesson  = Lesson.objects.all()

    return render(request, 'admin/')'''
