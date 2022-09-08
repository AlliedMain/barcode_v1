from django.urls import path
from . import views



app_name ='common'

urlpatterns = [
     path('', views.index, name = 'index'),
     path('user_profile/', views.user_profile, name='create_user_profile'),
     path('profile_view/', views.user_profile_view, name='profile_view'),
 ]
