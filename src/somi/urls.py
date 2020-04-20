from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('courses/', include('courses.urls')),

    # authentication urls
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
