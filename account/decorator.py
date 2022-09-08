from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
import six
from django.contrib.auth.decorators import user_passes_test

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('lms:portal')

        else:
            return view_func(request, *args, **kwargs)



    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exist():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('account:portal')

        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'teacher':
                return redirect('administration:')
            elif group == 'spela-admin':
                return view_func(request, *args, **kwargs)
            else:
                return redirect('lms:portal')
        else:
            return HttpResponse("You re not allowed")# <- return response here (possibly a redirect to login page?)

    return wrapper_function



def group_required(group, login_url=None,raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups =(group,)
        else:
            groups = group

        if user.groups.filter(permissions=groups).exists():
            return True

        if raise_exception:
            raise PermissionDenied

        return False

    return user_passes_test(check_perms, login_url=login_url)
