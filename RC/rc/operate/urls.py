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
   
    
    path('notice/', notice, name='notice'),
    path('publish/', publish, name='publish'),
    path('discount_rate/', discount_rate, name='discount_rate'),
    path('network/', network, name='network'),
    

### 유저관리 URL ########################################################
    path('users/', usersMyLV.as_view(), name='users'),
    path('get_like/', get_like, name='get_like'),
########################################################################

#### 가맹점 URL ########################################################
    path('approval/', ApprovalLV.as_view(), name='approval'),
    path('get_approval/', get_approval, name='get_approval'),
########################################################################


##### 차트 URL #########################################################
    path('statistics/', ChartHomeView.as_view(), name='statistics'),
    path('statistics/chartdata/', ChartData.as_view(), name='chartdata'),
    path('statistics/regional/',regional.as_view(),name='regional'),
    path('statistics/gender/',gender.as_view(),name='gender'),
    path('statistics/store/',store.as_view(),name='store'),
########################################################################
    
    ## login
    path('login_required/', login_required, name='login_required'),
]
