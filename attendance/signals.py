import logging
import datetime
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed


error_log=logging.getLogger('error')

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
        print('user {} logged in through page {}'.format(user.username, request.META.get('HTTP_REFERER')))
        try:
        login_logout_logs = LoginLogoutLog.objects.filter(session_key=request.session.session_key, user=user.id)[:1]
        if not login_logout_logs:
            login_logout_log = LoginLogoutLog(login_time=datetime.datetime.now(),session_key=request.session.session_key, user=user, host=request.META['HTTP_HOST'])
            login_logout_log.save()
        except Exception, e:
        # log the error
        error_log.error("log_user_logged_in request: %s, error: %s" % (request, e))

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
        print('user {} logged in failed through page {}'.format(credentials.get('username'), request.META.get('HTTP_REFERER')))



@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
        print('user {} logged out through page {}'.format(user.username, request.META.get('HTTP_REFERER')))
        from django.db import models
from django.contrib.auth.models import User

class LoginLogoutLog(models.Model):
    user = models.ForeignKey(User)
    session_key = models.CharField(max_length=100, blank=False, null=False)
    host = models.CharField(max_length=100, blank=False, null=False)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'login_logout_logs'
