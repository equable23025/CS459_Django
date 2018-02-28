"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('', views.current_datetime),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.login, {'template_name': 'myapp/registration/login.html'}, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('profiles/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('rent/', views.CreateRentView.as_view(), name='rent'),
    path('car/', views.ListCarView.as_view(), name='car'),
    path('logout/',auth_views.logout,{'template_name': 'myproject/templates/registration/logout.html'}, name='logout'),
]
