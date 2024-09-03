"""webcourt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from client import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),
    path('logout/', views.logout, name='logout'),
    path('mycase/', views.mycase, name='mycase'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('store_contact/', views.store_contact, name='store_contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('store_feedback/', views.store_feedback, name='store_feedback'),
    path('details_case/<int:id>', views.details_case, name='details_case'),
    path('about_us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('store_appointment/', views.store_appointment, name='store_appointment'),
    path('my_appointment/', views.my_appointment, name='my_appointment'),

    path('change_password/', views.change_password, name='change_password'),
    path('change_password_update/', views.change_password_update, name='change_password_update'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),

     
]

 
