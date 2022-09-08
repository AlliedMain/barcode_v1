from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, TeacherForm, PartnerForm, CreateUserForm
from .decorator import unauthenticated_user, admin_only
from .models import Student , Teacher, Partner
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group
from django.urls import reverse
from common.views import *
from django.contrib.auth import views as auth_views


# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='student')
            user.groups.add(group)
            return redirect("account:login")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "account/register.html",
                          context={"form":form})

    form = CreateUserForm
    return render(request = request,
                  template_name = "account/register.html",
                  context={"form":form})

def loginPage(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    #messages.info(request, f"You are now logged in as {username}")
                    return redirect('administration:admin_dash')
                else:
                    #messages = messages.get_messages(request)
                    return render(request, "account/login.html", context={'messages':messages.get_messages(request)})

            return render(request = request,
                        template_name = "account/login.html",
                        context={})


def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request, 'account/logout.html')


def student(request):
    student = Student.objects.all()
    #[f['first_name'] for f in first_name]
    #[f'f1', f'f2']

    #subjects = student.subscribed_to.set_all()
    #subject_list = subjects.count()

    context = {'student': student}
    return render(request,'account/studentList.html', context)


def teacher(request):
    teacher = Teacher.objects.all()


    #status = teacher.o.set_all()


    context = {'teacher': teacher}
    return render(request, 'account/teacherList.html', context)


def partner(request):
    partner = Partner.objects.all()

    #subscribed = partner.franschise_model.set_all()
    #subscription = subscribed.count()

    context = {'partner': partner}
    return render(request,'account/partnerList.html', context)

def create_student(request):

    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'account/add_student.html', context)


def create_teacher(request):

    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('Not working')

    context = {'form':form}
    return render(request, 'account/add_teacher.html', context)


def create_partner(request):

    form = PartnerForm()

    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account:partner_Brief")

    context = {'form': form}
    return render(request, 'account/add_franchise.html', context)

def update_student(request, pk):
    form = StudentForm()
    context = {'form': form}
    return render(request, 'account/add_student.html', context)

def update_teacher(request, pk):
    form = TeacherForm()
    context = {'form': form}
    return render(request, 'account/add_teacher.html', context)

def update_partner(request, pk):
    form = PartnerForm()
    context = {'form': form}
    return render(request, 'account/add_franchise.html', context)


def add_school(request):
    return render(request,'account/add_school.html')
