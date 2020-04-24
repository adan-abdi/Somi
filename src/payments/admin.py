from django.contrib import admin
from .models import Plan,Subscription,Transaction


admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Transaction)
# Register your models here.
