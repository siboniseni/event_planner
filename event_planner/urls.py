"""Main URL configuration for the event_planner project.

This module defines the URL patterns for the entire Django project,
including the admin site, and includes the URL configurations
from the events and user_auth applications.

It also serves media files in development mode (`settings.DEBUG` is True).

Reference:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
    Function views:
        1. Add an import:
            from my_app import views
        2. Add a URL to urlpatterns:
            path('', views.home, name='home')

    Class-based views:
        1. Add an import:
            from other_app.views import Home
        2. Add a URL to urlpatterns:
            path('', Home.as_view(), name='home')

    Including another URLconf:
        1. Import the include() function:
            from django.urls import include, path
        2. Add a URL to urlpatterns:
            path('blog/', include('blog.urls'))

:module: event_planner.urls
:author: Siboniseni Kasa
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('user_auth/', include('user_auth.urls')),
]

# In development, serve media files using Django
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



