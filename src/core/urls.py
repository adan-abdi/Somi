from django.conf import settings
from django.urls import path

from core.views import index
# from core.views import index, home

urlpatterns = [
    path('', index, name='index'),
    # path('', home, name='home'),
]
