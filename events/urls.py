"""URL configuration for the events application.

This module defines the URL patterns for the events app, including:
- Home page
- Event list
- Detailed view for a specific event
- Event posting form
- Past events archive

In development mode (`settings.DEBUG` is True), it also serves media files.

:module: events.urls
:author: Siboniseni Kasa
"""


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path("post_event/", views.post_event, name="post_event"),
    path('past-events/', views.past_events, name='past_events'),
]

if settings.DEBUG:  # Only serve media files via Django in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
