from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from courses.models import Courses


class Plan(models.Model):
    name = models.CharField(max_length=200)
    price_per_month = models.PositiveIntegerField()
    credits_per_month = models.PositiveIntegerField()

    class Meta:
        ordering = ['price_per_month']

    def __str__(self):
        return self.name


class Subscription(models.Model):
    plan = models.ForeignKey(
        Plan, related_name='subscriptionPlan', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='subscriber', on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField(default=timezone.now)
    end_timestamp = models.DateTimeField()

    class Meta:
        ordering = ['start_timestamp']

    def __str__(self):
        return f"{self.user}:{self.start_timestamp}->{self.end_timestamp}"


class Transaction(models.Model):
    payment_id = models.CharField(max_length=200)
    payment_type = models.CharField(max_lenght=200)
    payment_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        User, related_name='payer', on_delete=models.CASCADE)
    subscription = models.ForeignKey(
        User, related_name='subscribed', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    class Meta:
        ordering = ['payment_id']

    def __str__(self):
        return f"{self.user}:{self.amount}->{self.payment_date}"
