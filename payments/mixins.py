from django.shortcuts import redirect
from django.contrib import messages
from datetime import datetime
today = datetime.today()


class SubscriptionRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        subscription = request.user.subscription_set.filter(
            start_timestamp <= today, end_timestamp >= today).all()
        if len(subscription) > 0:
            return super().dispatch(request, *args, **kwargs)
        else:
            messages.error(
                request, 'Your Subscription or free trial has expired. Subscribe to continue learning')
            return redirect('/success/')
