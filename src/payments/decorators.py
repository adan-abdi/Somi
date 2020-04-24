#@subscription_required decorator algorithm
#from datetime import datetime
# today=datetime.today()
# use
# if len(subscription)==0
# redirect them to the subscription url with an alert to explain to the user
# else just pass
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages


def subscription_required(function):
    def wrap(request, *args, **kwargs):
        subscription = request.user.subscription_set.filter(
            start_timestamp <= today, end_timestamp >= today).all()
        if len(subscription) == 0:
            return function(request, *args, **kwargs)
        else:
            messages.error(request,'Your Subscription or free trial has expired. Subscribe to continue learning')
            return redirect('/success/')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
