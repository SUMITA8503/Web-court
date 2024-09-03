from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.models import User
from staff.models import *
from myadmin.models import *
from datetime import date
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings

def dashboard(request):
	context = {}
	return render(request, 'staff/dashboard.html',context)

def common_form(request):
	context = {}
	return render(request, 'staff/form.html',context)

def common_table(request):
	context = {}
	return render(request, 'staff/table.html',context)

def login(request):
	context = {}
	return render(request, 'staff/login.html',context)

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']


    result = auth.authenticate(username=username,password=password)

    if result is None:
         
        return redirect('/staff/login/')

    else:
        auth.login(request,result)
        return redirect('/staff/dashboard/')


def logout(request):
    auth.logout(request)
    return redirect('/staff/login')

def show_case(request):
    id = request.user.id
    staff_id = Staff.objects.get(user_id=id)
    result = Case.objects.filter(staff_id=staff_id)
    context = {'result':result}
    return render(request,'staff/show_case.html',context)


def details_case(request,id):
    result3 = Case.objects.get(pk=id)
    context = {'result3':result3}
    return render(request,'staff/detail_case.html',context)

def add_evidence(request):
    id = request.user.id
    staff_id = Staff.objects.get(user_id=id)
    result = Case.objects.filter(staff_id=staff_id)
    context = {'result':result}
    return render(request,'staff/add_evidence.html',context)

def store_evidence(request):
    mytitle = request.POST['title']
    mydescription = request.POST['description']
    myevidence = request.FILES['evidence']
    mycase = request.POST['case']




    mylocation = os.path.join(settings.MEDIA_ROOT, 'docs')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myevidence.name,myevidence)


    Document.objects.create(title=mytitle,description=mydescription,evidence=myevidence,case_id=mycase)
    return redirect('/staff/add_evidence/')

def details_evidence(request,id):
    result = Document.objects.filter(pk=id)
    context = {'result':result}
    return render(request,'staff/details_evidence.html',context)

def delete_evidence(request,id):
    result = Document.objects.get(pk=id)
    result.delete()
    return redirect('/staff/details_evidence/')

def edit_evidence(request,id):
    case = Case.objects.all()
    result = Document.objects.get(pk=id)
    
    context = {'result':result,'case':case}
    return render(request, 'staff/edit_evidence.html',context)

def update_evidence(request,id):
    mytitle = request.POST['title']
    mydescription = request.POST['description']
    myevidence = request.FILES['evidence']
    mycase = request.POST['case']




    mylocation = os.path.join(settings.MEDIA_ROOT, 'docs')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myevidence.name,myevidence)


    Document.objects.update_or_create(pk=id,defaults={'title':mytitle,'description':mydescription,'evidence':myevidence,'case_id':mycase})
    return redirect('/staff/details_evidence/')


def add_hearing(request):
    id = request.user.id
    staff_id = Staff.objects.get(user_id=id)
    result = Case.objects.filter(staff_id=staff_id)
    context = {'result':result}
    return render(request,'staff/add_hearing.html',context)

def store_hearing(request):
    mydate = request.POST['ndate']
    myremarks = request.POST['remarks']
    mystatus = request.POST['status']
    mycase = request.POST['case']

    Hearing.objects.create(nextdate=mydate,remarks=myremarks,status=mystatus,case_id=mycase)
    return redirect('/staff/add_hearing/')

def read_hearing(request,id):
    result = Hearing.objects.filter(pk=id)
    context = {'result':result}
    return render(request,'staff/read_hearing.html',context)

def delete_hearing(request,id):
    result = Hearing.objects.get(pk=id)
    result.delete()
    return redirect('/staff/read_hearing/')


def edit_hearing(request,id):
    case = Case.objects.all()
    result = Hearing.objects.get(pk=id)
    
    context = {'result':result,'case':case}
    return render(request, 'staff/edit_hearing.html',context)


def update_hearing(request,id):
    mydate = request.POST['ndate']
    myremarks = request.POST['remarks']
    mystatus = request.POST['status']
    mycase = request.POST['case']

    Hearing.objects.update_or_create(pk=id,defaults={'nextdate':mydate,'remarks':myremarks,'status':mystatus,'case_id':mycase})
    return redirect('/staff/read_hearing/')

def all_dates(request):
    result = Hearing.objects.all()
    context = {'result':result}
    return render(request,'staff/all_dates.html',context)

def all_details(request,id):
    result = Hearing.objects.get(pk=id)
    context = {'result':result}
    return render(request,'staff/all_details.html',context)

def edit_status(request,id):
    result = Hearing.objects.get(pk=id)
    context = {'result':result}
    return render(request,'staff/edit_status.html',context)

def update_status(request,id):

    myremarks = request.POST['remarks']
    mystatus = request.POST['status']


    Hearing.objects.update_or_create(pk=id,defaults={'description':myremarks,'status':mystatus})
    return redirect('/staff/all_dates/')


def change_password(request):
    context = {}
    return render(request,'staff/change_password.html',context)


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
            return redirect('/staff/login')
        else:
            messages.success(request, 'Invalid Password Try Again')
            return redirect('/staff/change_password/')     
    else:
         messages.success(request, 'Miss Match Password')


def edit_profile(request):
    id = request.user.id
    cities = City.objects.all()
    areas = Area.objects.all()
    result = Staff.objects.get(user_id=id)
    context={'result':result,'cities':cities,'areas':areas,}
    return render(request,'staff/edit_profile.html',context)


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
    Staff.objects.update_or_create(pk=id,defaults={'contact':contact,'address':address,'city_id':city,'area_id':area,'gender':gender})
    return redirect('/staff/edit_profile/')















