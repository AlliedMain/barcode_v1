from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import PIL
# Create your models here.

from django.db import models

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)



    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = [
        ('Shoe','Shoe'),
        ('Uniform','Uniform'),
        ]
    name = models.CharField(max_length=200, null = True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', null= True, blank= True)


    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Out for delivery',' Out for delivery'),
        ('Delivered', 'Delivered'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, null=False)
    refund_status = models.BooleanField(default=False , null=True)
    tags = models.ManyToManyField(Tag)
    order_status = models.CharField(max_length=30, null=False, choices=STATUS)


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null= False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
    @property
    def orders(self):
        order_count = self.order_set.all().count()
        return str(order_count)
