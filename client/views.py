from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.models import User
from myadmin.models import *
from staff.models import *
from client.models import *
from datetime import date
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.

def dashboard(request):
    context = {}
    return render(request, 'client/dashboard.html',context)

def login(request):
    context = {}
    return render(request, 'client/login.html',context)
    

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']


    result = auth.authenticate(username=username,password=password)

    if result is None:
         
        return redirect('/client/login/')

    else:
        auth.login(request,result)
        return redirect('/client/dashboard/')


def logout(request):
    auth.logout(request)
    return redirect('/client/login')


def add_contact(request):
    context = {}
    return render(request,'client/add_contact.html',context)

def store_contact(request):
    myname = request.POST['name']
    myemail = request.POST['email']
    mycon = request.POST['con']
    mymessage = request.POST['message']

    Contact.objects.create(name=myname,email=myemail,contact=mycon,message=mymessage)
    return redirect('/client/add_contact/')



def mycase(request):
    id = request.user.id
    client = Client.objects.get(user_id=id)
    result = Case.objects.filter(client_id=client.id)
    context = {'result':result}
    return render(request, 'client/mycase.html',context)

def details_case(request,id):
    result = Case.objects.get(pk=id)
    docs = Document.objects.filter(case_id=id)
    hear = Hearing.objects.filter(case_id=id)
    context = {'result':result,'docs':docs}
    return render (request , 'client/details_case.html',context)


def feedback(request):
    context = {}
    return render(request,'client/feedback.html',context)

def store_feedback(request):
    myrating = request.POST['rating']
    mycomment = request.POST['comment']
    id = request.user.id

    Feedback.objects.create(rating=myrating,comment=mycomment,user_id=id)
    

    return redirect('/client/feedback/')

def about_us(request):
    context = {}
    return render(request,'client/about_us.html',context)

def services(request):
    context = {}
    return render(request,'client/services.html',context)

def appointment(request):
    context = {}
    return render(request,'client/appointment.html')

def store_appointment(request):
    mysubject = request.POST['subject']
    mydescription = request.POST['description']
    id = request.user.id


    Appointment.objects.create(subject=mysubject,description=mydescription,user_id=id)
    return redirect('/client/appointment/')


def my_appointment(request):
    id = request.user.id
    result = Appointment.objects.filter(user_id=id)
    context = {'result':result}
    return render(request,'client/my_appointment.html',context)


def change_password(request):
    context = {}
    return render(request,'client/change_password.html',context)

def change_password_update(request):
    username = request.user.username
    old_password  = request.POST['old_password']
    new_password  = request.POST['new_password']
    rnew_password = request.POST['rnew_password']

    if new_password == rnew_password:
        user = auth.authenticate(username=username, password=old_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password Updated Successfully')
            return redirect('/client/login')
        else:
            messages.success(request, 'Invalid Password Try Again')
            return redirect('/client/change_password/')     
    else:
         messages.success(request, 'Miss Match Password')


def edit_profile(request):
    id = request.user.id
    cities = City.objects.all()
    areas = Area.objects.all()
    result = Client.objects.get(user_id=id)
    context={'result':result,'cities':cities,'areas':areas,}
    return render(request,'client/edit_profile.html',context)


def update_profile(request,id):
    id1 = request.user.id

    fname = request.POST['fname']
    lname = request.POST['lname']
    username = request.POST['username']
    email = request.POST['email']

    contact = request.POST['contact']
    address = request.POST['address']
    gender = request.POST['gender']
    area = request.POST['area']
    city = request.POST['city']

    user = User.objects.update_or_create(pk=id1,defaults={'first_name':fname,'last_name':lname,'email':email,'username':username,})
    Client.objects.update_or_create(pk=id,defaults={'contact':contact,'address':address,'city_id':city,'area_id':area,'gender':gender})
    return redirect('/client/edit_profile/')