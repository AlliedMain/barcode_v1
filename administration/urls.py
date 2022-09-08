from django.urls import path
from . import views

app_name ='administration'

urlpatterns = [
     path('admin_dash/', views.admin_view, name = 'admin_dash'),

]
