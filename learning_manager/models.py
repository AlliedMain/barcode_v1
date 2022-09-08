from django.db import models
from django.contrib.auth.models import User
#from memberships.models import UserMembership
from account.models import Partner, Teacher, Student





# Create your models here.


class Subject(models.Model):
    CATEGORY = [
        ('Seeds','Seeds'),
        ('Sprouts','Sprouts'),
        ]

    title = models.CharField(max_length=54, null=False, unique=True)
    spela_branch = models.CharField(max_length=10, null=False, choices=CATEGORY)
    creator = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    description = models.TextField(max_length=54, null=False)
    video_url = models.CharField(max_length=100)
    slug = models.SlugField()
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):

    slug = models.SlugField()
    title = models.CharField(max_length=30)
    creator = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course  = models.ManyToManyField(Subject)
    video_id = models.CharField(max_length=20)
    position = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
