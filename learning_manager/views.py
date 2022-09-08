from django.shortcuts import render,redirect
#from django.views.generic import views
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Subject, Lesson
from .forms import  SubjectForm,     LessonForm
from account.decorator import unauthenticated_user
# Create your views here.



def create_subject(request):

    form = SubjectForm()

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('Not working')

    context = {'form':form}
    return render(request, 'lms/create_subject.html', context)




def create_lesson(request):

    form = LessonForm()

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse('Not working')

    context = {'form':form}
    return render(request, 'lms/create_lesson.html', context)


    #****************************************************List View*************************************************************

def portal(request):
    subject = Subject.objects.all().order_by('-video_url')[0:5]
    lesson = Lesson.objects.all()

    #total_subjects = subject.objects.all().count()

    #total_lessons = lesson.objects.all().count()
    #active = Subject.objects.filter(title='Science').count()
    #pending = Lesson.objects.filter(slug='all').count()



    context = {'subject':subject, 'lesson':lesson}
    #'total_subjects':total_subjects,'total_lessons':total_lessons,
    #'active':active, 'pending':pending
    return render(request, 'lms/lms.html', context)




def subjects(request):
    subjects = Subject.objects.all
    context = {'subjects':subjects}
    return render(request, 'lms/subject_list_view.html', context)






def lesson(request):
    lessons = Lesson.objects.all
    context = {'lessons':lessons}
    return render(request, 'lms/lesson_list_view.html', context)




    lessons = lessons.filter(category=title)


    context = {'subject':subjects, 'lessons':lessons, 'total_lessons':total_lessons}
    return render(request, 'lms/lesson_list_view.html', context)




def attendance(request):
    return redirect('/attendance/attendance.html')

def games(request):
    return render( request,'lms/game.html')


def ai_edge_device(request):
    return render(request,'lms/ai_edge_device.html')
