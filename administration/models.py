from django.db import models
#import signals_handler.py

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class LoginLogoutLog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, blank=False, null=False)
    host = models.CharField(max_length=100, blank=False, null=False)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'login_logout_logs'
