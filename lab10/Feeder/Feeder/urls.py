"""Feeder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from backend.views import *
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout, {'next_page': '/'}),
    url(r'^createfeedbackform/', createfeedbackform),
    url(r'^register/', register),
    url(r'^success/', registersuccess),
    url(r'^adminlogin/', adminlogin),
    url(r'^adminhome/', adminhome),
    url(r'^adminlogout/', adminlogout),
    url(r'^studentlogin/', studentlogin),
    # url(r'^facebooklogin/', facebooklogin),
    # url(r'^adminhome/viewcourses/', viewcourses)
    # url(r'^viewfeedback/', viewfeedback),
    # url(r'^studentlogout/', studentlogout)
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]