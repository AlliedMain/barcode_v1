from django.urls import path
from . import views


app_name = 'lms'

urlpatterns = [
    path('create_subject/', views.create_subject, name='create_subjects'),
    path('create_lesson/', views.create_lesson, name='create_lesson'),
    path('portal/', views.portal, name='portal'),
    path('subject/', views.subjects, name='subject'),
    path('lesson/', views.lesson, name='lesson'),
    path('attendance/', views.attendance, name='attendance'),
    path('games/', views.games, name='games'),
    path('ai_edge/', views.ai_edge_device, name='ai_edge'),
]
