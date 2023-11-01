"""
URL configuration for crud3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('admin_pannel',views.admin_site),
    path('add',views.add),
    path('show',views.show),
    path('update/<id>/',views.update_record),
    path('delete/<id>/',views.delete_record),
    path('login',views.user_login),
    path('register',views.user_register),
    path('engineer',views.engineer),
    path('doctor',views.doctor),
    path('logout',views.user_logout),
    path('mail/<id>',views.SendMail),
]
