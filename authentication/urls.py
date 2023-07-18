from rest_framework.authtoken import views
from django.urls import path
from .views import *

urlpatterns = [
    path('login', views.obtain_auth_token),
    path('reg',Registration),
    path('del',delete_user),
]