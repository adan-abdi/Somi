from django.conf import settings
from django.urls import path

from core.views import home

urlpatterns = [
    path('', home, name='home'),
]
