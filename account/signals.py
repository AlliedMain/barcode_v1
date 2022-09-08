from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import  Teacher , Student, Partner
from django.contrib.auth.models import Group
from common.views import user


def student_profile(sender , instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='student')
        instance.group.add(group)
        Student.objects.created(
            user=instance
            name=instance.username,
            )
        print('Profile_Created')
post_save.connect(student_profile, sender=User)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.user_profile.save()
