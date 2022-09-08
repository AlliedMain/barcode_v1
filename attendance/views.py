from django.shortcuts import render
from .models import *
from account.decorator import unauthenticated_user


# Create your views here.


def attendance(request):

    attendance = LoginLogoutLog.objects.all()

    context ={'attendance':attendance}
    return render(request, 'attendance/attendance.html', context)
