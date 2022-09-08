from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings


app_name = "inventory"
urlpatterns = [
    path('', views.dashBoard, name="dashboard"),
    path('products/', views.products, name="products"),
    path('customer/', views.customer, name="customer"),

    #------------ (CREATE URLS) ------------
    path('create_order/', views.createOrder, name="create_order"),
    path('create_product/', views.createproduct, name="create_product"),

    #------------ (UPDATE URLS) ------------
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),


    #------------ (UPDATE URLS) ------------
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
