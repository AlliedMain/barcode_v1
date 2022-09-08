from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name='account'

urlpatterns =[

        path('register/', views.registerPage, name='register'),
        path('login/', views.loginPage, name='login'),
        path('logout/', views.logoutUser, name='logout'),
        path('student/', views.student, name='student_Brief'),
        path('schools/', views.add_school, name='schools'),
        path('teacher/', views.teacher, name='teacher_Brief'),
        path('create_student/', views.create_student, name='create_student'),
        path('create_teacher/', views.create_teacher, name='create_teacher'),
        path('create_partner/', views.create_partner, name='create_partner'),
        path('partner/', views.partner, name='partner_Brief'),
        path('update_student<str:pk>/', views.update_student, name='update_student'),
        path('update_teacher/<str:pk>', views.update_teacher, name='update_teacher'),
        path('update_partner/<str:pk>', views.update_partner, name='update_partner'),
        path('reset_password/', auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"), name="reset_password"),
        path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name="account/password_email_sent.html"), name="reset_password_done"),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/confirm_password.html"), name="reset_password_confirm"),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name="password_reset_complete"),

]
