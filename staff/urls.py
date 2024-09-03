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
from staff import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('common_form', views.common_form, name='common_form'),
    path('common_table', views.common_table, name='common_table'),
    path('login', views.login, name='login'),
    path('login_check/', views.login_check, name='login_check'),
    path('logout/', views.logout, name='logout'),


    #case
    path('show_case/', views.show_case, name='show_case'),
    path('details_case/<int:id>', views.details_case, name='details_case'),
    path('add_evidence/', views.add_evidence, name='add_evidence'),
    path('store_evidence/', views.store_evidence, name='store_evidence'),
    path('details_evidence/<int:id>', views.details_evidence, name='details_evidence'),
    path('delete_evidence/<int:id>', views.delete_evidence, name='delete_evidence'),
    path('edit_evidence/<int:id>', views.edit_evidence, name='edit_evidence'),
    path('update_evidence/<int:id>', views.update_evidence, name='update_evidence'),


    #hearing
    path('add_hearing/', views.add_hearing, name='add_hearing'),
    path('store_hearing/', views.store_hearing, name='store_hearing'),
    path('read_hearing/<int:id>', views.read_hearing, name='read_hearing'),
    path('delete_hearing/<int:id>', views.delete_hearing, name='delete_hearing'),
    path('edit_hearing/<int:id>', views.edit_hearing, name='edit_hearing'),
    path('update_hearing/<int:id>', views.update_hearing, name='update_hearing'),
    path('all_dates/', views.all_dates, name='all_dates'),
    path('all_details/<int:id>', views.all_details, name='all_details'),
    path('edit_status/<int:id>', views.edit_status, name='edit_status'),
    path('update_status/<int:id>', views.update_status, name='update_status'),

    path('change_password/', views.change_password, name='change_password'),
    path('change_password_update/', views.change_password_update, name='change_password_update'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),


]
