"""rc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.auth import views as auth_views

app_name = 'operate'

urlpatterns = [
    path('main/', main, name='main'),
    path('dashboard/', dashboard, name='dashboard'),
    path('users/', usersMyLV.as_view(), name='users'),
    path('approval/', ApprovalLV.as_view(), name='approval'),
    path('notice/', notice, name='notice'),
    path('publish/', publish, name='publish'),
    path('discount_rate/', discount_rate, name='discount_rate'),
    path('network/', network, name='network'),
    path('statistics/', statistics, name='statistics'),
    path('get_like/', get_like, name='get_like'),
    path('get_approval/', get_approval, name='get_approval'),

    ## login
    path('login_required/', login_required, name='login_required'),
]
