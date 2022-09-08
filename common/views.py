from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from common.forms import UserForm , UserProfileInForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from account.decorator import  unauthenticated_user, admin_only
from .models import *
from django.contrib.auth.models import User
# Create your views here.


#@login_required(login_url='account:login')
#@admin_only
def index(request):
    return render(request, 'index.html')



def user_profile(request):
    form = UserProfileInForm()

    if request.method=="POST":

        form = UserProfileInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form':form}
    return render(request, 'profile_form.html', context)




@unauthenticated_user
def user_profile_view(request):
    # check if the user is_authenticated:
    profile = User_profile.objects.get(id=request.user.name)
    context = {
        'profile': profile
    }
    return render(request, 'user_profile.html', context)
