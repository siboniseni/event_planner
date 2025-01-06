from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.register, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]