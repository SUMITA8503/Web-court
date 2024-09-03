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
from myadmin import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('common_form', views.common_form, name='common_form'),
    path('common_table', views.common_table, name='common_table'),
    path('login', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),
    path('logout/', views.logout, name='logout'),
   
    path('inquiry', views.inquiry, name='inquiry'),
    path('delete_inq/<int:id>', views.delete_inq, name='delete_inq'),

    path('feedback', views.feedback, name='feedback'),
    path('delete_fed/<int:id>', views.delete_fed, name='delete_fed'),
    path('clients', views.clients, name='clients'),


    #state
    path('add_state', views.add_state, name='add_state'),
    path('store_state', views.store_state, name='store_state'),
    path('all_state', views.all_state, name='all_state'),
    path('delete_state/<int:id>', views.delete_state, name='delete_state'),
    path('edit_state/<int:id>', views.edit_state, name='edit_state'),
    path('update_state/<int:id>', views.update_state, name='update_state'),

    path('add_city', views.add_city, name='add_city'),
    path('store_city', views.store_city, name='store_city'),
    path('all_city', views.all_city, name='all_city'),
    path('delete_city/<int:id>', views.delete_city, name='delete_city'),
    path('edit_city/<int:id>', views.edit_city, name='edit_city'),
    path('update_city/<int:id>', views.update_city, name='update_city'),

    path('add_area', views.add_area, name='add_area'),
    path('store_area', views.store_area, name='store_area'),
    path('all_area', views.all_area, name='all_area'),
    path('delete_area/<int:id>', views.delete_area, name='delete_area'),
    path('edit_area/<int:id>', views.edit_area, name='edit_area'),
    path('update_area/<int:id>', views.update_area, name='update_area'),

    #Staff
    path('add_staff/', views.add_staff, name='add_staff'),
    path('store_staff', views.store_staff, name='store_staff'),
    path('read_staff', views.read_staff, name='read_staff'),
    path('details_staff/<int:id>', views.details_staff, name='details_staff'),
    path('delete_staff/<int:id>', views.delete_staff, name='delete_staff'),
    path('edit_staff/<int:id>', views.edit_staff, name='edit_staff'),
    path('update_staff/<int:id>', views.update_staff, name='update_staff'),

    #client
    path('add_client/', views.add_client, name='add_client'),
    path('store_client', views.store_client, name='store_client'),
    path('read_client', views.read_client, name='read_client'),
    path('details_client/<int:id>', views.details_client, name='details_client'),
    path('delete_client/<int:id>', views.delete_client, name='delete_client'),
    path('edit_client/<int:id>', views.edit_client, name='edit_client'),
    path('update_client/<int:id>', views.update_client, name='update_client'),

    #case
    path('add_case/', views.add_case, name='add_case'),
    path('store_case/', views.store_case, name='store_case'),
    path('read_case/', views.read_case, name='read_case'),
    path('details_case/<int:id>', views.details_case, name='details_case'),
    path('delete_case/<int:id>', views.delete_case, name='delete_case'),
    path('edit_case/<int:id>', views.edit_case, name='edit_case'),
    path('update_case/<int:id>', views.update_case, name='update_case'),


    path('edit_status/<int:id>', views.edit_status, name='edit_status'),
    path('update_status/<int:id>', views.update_status, name='update_status'),
    path('read_appointment/', views.read_appointment, name='read_appointment'),
    path('accept_ap/<int:id>', views.accept_ap, name='accept_ap'),
    path('store_ap/<int:id>', views.store_ap, name='store_ap'),
    path('reject_ap/', views.reject_ap, name='reject_ap'),
    path('reject_reason/', views.reject_reason, name='reject_reason'),


    path('all_dates/', views.all_dates, name='all_dates'),





    path('search_case/', views.search_case, name='search_case'),
    path('change_password/', views.change_password, name='change_password'),
    path('change_password_update/', views.change_password_update, name='change_password_update'),











]
