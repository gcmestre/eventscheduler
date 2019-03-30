from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


app_name = 'authentication'
urlpatterns = [
    path('signup', signup_view, name='signup'),
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]