from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
# Create your models here.

def path_and_rename(instance, filename):
    upload_to ='images/'
    ext = filename.split(',')[-1]
    #get file name
    if instance.user.username:
        filename = 'User_Profile_pictures/{},{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)




class User_profile(models.Model):
    GENDER ={
        ('male', 'male'),
        ('female','female')
        }
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    franchise = 'partner'

    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
        (franchise, 'partner'),
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='female')
    address_1 = models.CharField(max_length=20, blank=True)
    address_2 = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)

    user_type = models.CharField(max_length=10, choices=user_types, default=student)
    state = models.CharField(max_length=30, blank=True)
    postcode = models.IntegerField(default='122001')
    bio = models.CharField(max_length=150, blank=True)
    profile_Pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture", blank=True)

    

    def __str__(self):
        return self.user.username + 'User_profile'

    #def save(self, *args, **kwargs):
        #super().save(*args,**kwargs)


class Requests(models.Model):
    profile = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    mobile_number = models.CharField(max_length=15)


    def __str__(self):
        return self.profile.user.username
