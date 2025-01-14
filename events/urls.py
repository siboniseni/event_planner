from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('events/', views.event_list, name='event_list'),  # Event list page
    path('event/<int:pk>/', views.event_detail, name='event_detail'),  # Event detail page
    path("post_event/", views.post_event, name="post_event"),
    path('past-events/', views.past_events, name='past_events'),
]

if settings.DEBUG:  # Only serve media files via Django in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
