from django.db import models
from django.contrib.auth.models import User
from common.models import User_profile
# Create your models here.
from django.utils import timezone
#from lms.models import *
def path_and_rename(instance, filename):
    upload_to ='Images/'
    ext = filename.split(',')[-1]
    #get file name
    if instance.user.username:
        filename = 'User_Profile_pictures/{},{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)



class Teacher(models.Model):
    prefixes = (
            ('mr', 'Mr'),
            ('mrs', 'Mrs'),
    )
    title = models.CharField(max_length=48, null=False,choices=prefixes)
    first_name = models.CharField(max_length=64,null=False, blank=False)
    last_name = models.CharField(max_length=64,null=True, blank=True)
    gender = models.CharField(max_length=1, default='F')
    educational_qualification = models.CharField(max_length=64)
    professional_details = models.CharField(max_length=82)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    #created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by')
    #location_id = models.ForeignKey("users.Location", on_delete=models.SET_NULL, null=True, blank=True)
    user_profile = models.ForeignKey(User_profile, on_delete=models.CASCADE, null=False, blank=False)

    mobile_no = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=255, unique=True)
    tutor_id = models.CharField(max_length=20, null=False, blank=True)
    dob = models.DateField(null=True, blank=True)
    pan = models.CharField(max_length=10, null=True, blank=True)
    created_timestamp = models.DateTimeField(max_length=23, default=timezone.now)

    def __str__(self):
        return self.first_name


class Partner(models.Model):
    title_choices = (
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
        ('Mrs', 'Mrs'),
        ('Dr', 'Dr'),
    )

    educational_choices =(
        ('Doctorate','Doctorate'),
        ('Post-Graduate','Post-Graduate'),
        ('Graduate','Graduate'),
        ('Intermediate','Intermediate'),
        ('Matric','Matric'),
        ('None','None')
    )

    current_occupation =(
        ('Business','Business'),
        ('Self Employed','Self Employed'),
        ('Professional','Profess2ional'),
        ('Govt_services','Govt_services'),
        ('Pvt_services','Pvt-services'),
    )

    franchise_choices = (
        ('Spela-studio','Studio'),
        ('Spela-Smart','Smart'),
        ('Spela-first','First'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #zone = models.ForeignKey(Zones, on_delete=models.SET_NULL, null=True, blank=True)


    mobile_no = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=255, unique=True)
    day_phone = models.CharField(max_length=15, null=True, blank=True)
    pan = models.CharField(max_length=10, null=True, blank=False)
    gst = models.CharField(max_length=21, null=True, blank=False)


    permanent_address = models.CharField(max_length=15 , null=True, blank=True)
    communication_address = models.CharField(max_length=15 , null=True, blank=True)
    job = models.CharField(max_length=15,null=True, blank=True)


    first_name = models.CharField(max_length=24,null=True, blank=True)
    last_name = models.CharField(max_length=25,null=True, blank=True)
    gender = models.CharField(max_length=1, default='M')
    martial_status = models.CharField(max_length=16, blank=True, null=True)
    title =  models.CharField(max_length=15, choices=title_choices)
    educational_qualification = models.CharField(max_length=64, choices=educational_choices)
    professional_details = models.CharField(max_length=82, choices=current_occupation)
    franschise_model = models.CharField(max_length=22, choices=franchise_choices, default='studio')


    #created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by')
    #location_id = models.ForeignKey("users.Location", on_delete=models.SET_NULL, null=True, blank=True)
    created_timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.user


class Student(models.Model):
    franchise_choices = (
        ('Spela-studio','Seeds'),
        ('Spela-Smart','Sprouts'),
        ('Spela-first','Blooms'),
        )
    first_name = models.CharField(max_length=64,null=False, blank=False)
    last_name = models.CharField(max_length=64,null=True, blank=True)
    gender = models.CharField(max_length=1, default='F')
    date_of_birth = models.DateField()
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_to = models.CharField(max_length=30, null=False,choices=franchise_choices)
    gaurdian_name = models.CharField(max_length=64,null=False, blank=False)
    gaurdian_phone_no = models.CharField(max_length=11, null=False, unique=True)
    registered_email = models.EmailField(blank=True, null=False)

    #course_assigned = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #lesson_progress_status = models.ForeignKey(Lesson, on_delte=models.CASCADE)


    def __str__(self):
        return self.first_name
