from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'user_auth'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('authenticate_user/', views.authenticate_user, 
         name='authenticate_user'),
    path('signup/', views.register, name='signup'),
]