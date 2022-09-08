from django.shortcuts import render,redirect
from memberships.models import Membership,UserMembership,Subscription
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User


def membership(request):
    premium = UserMembership.objects.all()
    context = {'premium':premium}
    return render(request, 'memberships/payment.html', context)
