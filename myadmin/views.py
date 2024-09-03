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

def login(request):
    context = {}
    return render(request, 'myadmin/login.html',context)


def login_check(request):
    username = request.POST['username']
    password = request.POST['password']


    result = auth.authenticate(username=username,password=password)

    if result is None:
         
        return redirect('/myadmin/login/')

    else:
        auth.login(request,result)
        return redirect('/myadmin/dashboard/')


def logout(request):
    auth.logout(request)
    return redirect('/myadmin/login')

def dashboard(request):
    context = {}
    return render(request, 'myadmin/dashboard.html',context)

def common_form(request):
    context = {}
    return render(request, 'myadmin/form.html',context)

def common_table(request):
    context = {}
    return render(request, 'myadmin/table.html',context)


#state
def add_state(request):
    context = {}
    return render(request, 'myadmin/add_state.html',context)

def store_state(request):
    name = request.POST['name']
    print(name)
    State.objects.create(state_name=name)
    return redirect('/myadmin/add_state')

def all_state(request):
    result = State.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/all_state.html',context)

def delete_state(request,id):
    result = State.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_state')

def edit_state(request,id):
    result = State.objects.get(pk=id)
    context = {'result':result}
    return render(request, 'myadmin/edit_state.html',context)

def update_state(request,id):
    name = request.POST['name']
    State.objects.update_or_create(pk=id,defaults={'state_name':name})
    return redirect('/myadmin/all_state')


def add_city(request):
    result = State.objects.all()
    context = {'states':result}
    return render(request, 'myadmin/add_city.html',context)

def store_city(request):
    name = request.POST['name']
    state_id = request.POST['state_id']
    print(name)
    City.objects.create(city_name=name,state_id=state_id)
    return redirect('/myadmin/add_city')

def all_city(request):
    result = City.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/all_city.html',context)

def delete_city(request,id):
    result = City.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_city')

def edit_city(request,id):
    result = City.objects.get(pk=id)
    states = State.objects.all()
    context = {'states':states,'result':result}
    return render(request, 'myadmin/edit_city.html',context)

def update_city(request,id):
    name = request.POST['name']
    state_id = request.POST['state_id']

    data = {
              'city_name' : name,
              'state_id':state_id
           }
  
    City.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_city')

def add_area(request):
    result2 = City.objects.all()
    context = {'cities':result2}
    return render(request, 'myadmin/add_area.html',context)

def store_area(request):
    name = request.POST['name']
    city_id = request.POST['city_id']
    Area.objects.create(area_name=name,city_id=city_id)
    return redirect('/myadmin/add_area')

def all_area(request):
    result = Area.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/all_area.html',context)

def delete_area(request,id):
    result = Area.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/all_area')

def edit_area(request,id):
    result = Area.objects.get(pk=id)
    cities = City.objects.all()
    context = {'cities':cities,'result':result}
    return render(request, 'myadmin/edit_area.html',context)

def update_area(request,id):
    name = request.POST['name']
    city_id = request.POST['city_id']

    data = {
              'area_name' : name,
              'city_id':city_id
           }
  
    Area.objects.update_or_create(pk=id,defaults=data)
    return redirect('/myadmin/all_area')



# staff views
def add_staff(request):
    areas = Area.objects.all()
    cities = City.objects.all()
    context = {'areas':areas,'cities':cities}
    return render(request, 'myadmin/add_staff.html',context)

def store_staff(request):
    myfname = request.POST['fname']
    mylname = request.POST['lname']
    myemail = request.POST['email']
    myusername = request.POST['username']
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    mycontact = request.POST['contact']
    mygender  = request.POST['gender']
    myaddress = request.POST['address']
    myimage    = request.FILES['image']
    mycity     =  request.POST['city']
    myarea     = request.POST['area']


    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)

    if password == cpassword:
        user = User.objects.create_user(first_name=myfname,last_name=mylname,email=myemail,username=myusername,password=password)
   
        Staff.objects.create(contact=mycontact,address=myaddress,gender=mygender,image=myimage,city_id=mycity,area_id=myarea,user_id=user.id)
        return redirect('/myadmin/add_staff/')

    else:
        print('Password and confirm password mismatched')

    

     

def read_staff(request):
    wow = Staff.objects.all()
    context = {'wow': wow}
    return render (request , 'myadmin/read_staff.html',context)

def details_staff(request,id):
    result = Staff.objects.get(pk=id)
    context = {'result': result}
    return render (request , 'myadmin/details_staff.html',context)

def delete_staff(request,id):
    result = Staff.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/read_staff')

def edit_staff(request,id):
    result = Staff.objects.get(pk=id)
    cities = City.objects.all()
    areas = Area.objects.all()
    context = {'cities':cities,'result':result,'areas':areas}
    return render(request, 'myadmin/edit_staff.html',context)

def update_staff(request,id):
    myfname = request.POST['fname']
    mylname = request.POST['lname']
    myemail = request.POST['email']
    myusername = request.POST['username']
    mycontact = request.POST['contact']
    mygender  = request.POST['gender']
    myaddress = request.POST['address']
    myimage    = request.FILES['image']
    mycity     =  request.POST['city']
    myarea     = request.POST['area']


    mylocation = os.path.join(settings.MEDIA_ROOT, 'upload')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)

    user = User.objects.update_or_create(pk=id,defaults={'first_name':myfname,'last_name':mylname,'email':myemail,'username':myusername,'password':mycontact})

    Staff.objects.update_or_create(pk=id,defaults={'contact':mycontact,'address':myaddress,'gender':mygender,'image':myimage,'city_id':mycity,'area_id':myarea})
    return redirect('/myadmin/read_staff')

#client
def add_client(request):
    areas = Area.objects.all()
    cities = City.objects.all()
    context = {'areas':areas,'cities':cities}
    return render(request, 'myadmin/add_client.html',context)

def store_client(request):
    myfname = request.POST['fname']
    mylname = request.POST['lname']
    myemail = request.POST['email']
    myusername = request.POST['username']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    
    mycontact = request.POST['contact']
    mygender  = request.POST['gender']
    myaddress = request.POST['address']
    myimage    = request.FILES['image']
    mycity     =  request.POST['city']
    myarea     = request.POST['area']


    mylocation = os.path.join(settings.MEDIA_ROOT, 'uploaded')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)

    if password == cpassword:
        user = User.objects.create_user(first_name=myfname,last_name=mylname,email=myemail,username=myusername,password=password)
   
        Client.objects.create(contact=mycontact,address=myaddress,gender=mygender,image=myimage,city_id=mycity,area_id=myarea,user_id=user.id)
        return redirect('/myadmin/add_client/')

    else:
        print('Password and confirm password mismatched')

     

def read_client(request):
    wow1 = Client.objects.all()
    context = {'wow1': wow1}
    return render (request , 'myadmin/read_client.html',context)

def details_client(request,id):
    result = Client.objects.get(pk=id)
    context = {'result': result}
    return render (request , 'myadmin/details_client.html',context)

def delete_client(request,id):
    result = Client.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/read_client')

def edit_client(request,id):
    result = Client.objects.get(pk=id)
    cities = City.objects.all()
    areas = Area.objects.all()
    context = {'cities':cities,'result':result,'areas':areas}
    return render(request, 'myadmin/edit_client.html',context)

def update_client(request,id):
    myfname = request.POST['fname']
    mylname = request.POST['lname']
    myemail = request.POST['email']
    mycontact = request.POST['contact']
    mygender  = request.POST['gender']
    myaddress = request.POST['address']
    myimage    = request.FILES['image']
    mycity     =  request.POST['city']
    myarea     = request.POST['area']


    mylocation = os.path.join(settings.MEDIA_ROOT, 'client')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myimage.name,myimage)

    Client.objects.update_or_create(pk=id,defaults={'fname':myfname,'lname':mylname,'email':myemail,'contact':mycontact,'gender':mygender,'address':myaddress,'image':myimage,'city_id':mycity,'area_id':myarea})
    return redirect('/myadmin/read_client')

#case

def add_case(request):
    areas = Area.objects.all()
    cities = City.objects.all()
    clients = Client.objects.all()
    staffs = Staff.objects.all()
    context = {'areas':areas,'cities':cities,'clients':clients,'staffs':staffs}
    return render(request, 'myadmin/add_case.html',context)

def store_case(request):
    mytitle = request.POST['title']
    mydescription = request.POST['description']
    mycrimetype = request.POST['type']
    myfir_date = request.POST['fir_date']
    myfir_station = request.POST['fir_station']
    myfir_copy = request.FILES['fir_copy']
    mycity = request.POST['city']
    myarea = request.POST['area']
    myclient = request.POST['client']
    mystaff = request.POST['staff']

    mylocation = os.path.join(settings.MEDIA_ROOT, 'copy')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfir_copy.name,myfir_copy)


    Case.objects.create(title=mytitle,description=mydescription,crimetype=mycrimetype,fir_date=myfir_date,fir_station=myfir_station,fir_copy=myfir_copy,city_id=mycity,area_id=myarea,client_id=myclient,staff_id=mystaff)
    return redirect('/myadmin/add_case/')


def read_case(request):
    result = Case.objects.all()
    context = {'result': result}
    return render (request , 'myadmin/read_case.html',context)

def details_case(request,id):
    result3 = Case.objects.get(pk=id)
    context = {'result3':result3}
    return render(request,'myadmin/details_case.html',context)

def delete_case(request,id):
    result = Case.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/read_case')

def edit_case(request,id):
    result = Case.objects.get(pk=id)
    cities = City.objects.all()
    areas = Area.objects.all()
    clients = Client.objects.all()
    staffs = Staff.objects.all()
    context = {'cities':cities,'result':result,'areas':areas,'clients':clients,'staffs':staffs}
    return render(request, 'myadmin/edit_case.html',context)

def update_case(request,id):
    mytitle = request.POST['title']
    mydescription = request.POST['description']
    mycrimetype = request.POST['type']
    myfir_date = request.POST['fir_date']
    myfir_station = request.POST['fir_station']
    myfir_copy = request.FILES['fir_copy']
    mycity = request.POST['city']
    myarea = request.POST['area']
    myclient = request.POST['client']
    mystaff = request.POST['staff']

    mylocation = os.path.join(settings.MEDIA_ROOT, 'copy')
    obj = FileSystemStorage(location=mylocation)
    obj.save(myfir_copy.name,myfir_copy)


    Case.objects.update_or_create(pk=id,defaults={'title':mytitle,'description':mydescription,'crimetype':mycrimetype,'fir_date':myfir_date,'fir_station':myfir_station,'fir_copy':myfir_copy,'city_id':mycity,'area_id':myarea,'client_id':myclient,'staff_id':mystaff})
    return redirect('/myadmin/read_case/')


def edit_status(request,id):
    result = Case.objects.get(pk=id)
    context = {'result':result}
    return render(request,'myadmin/update_status.html',context)

def update_status(request,id):
    myremarks = request.POST['remarks']
    mystatus = request.POST['status']


    Case.objects.update_or_create(pk=id,defaults={'remarks':myremarks,'status':mystatus})
    return redirect('/myadmin/read_case/')







def inquiry(request):
    result = Contact.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/inquiry.html',context)

def delete_inq(request,id):
    result = Contact.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/inquiry')


def feedback(request):
    result = Feedback.objects.all()
    context = {'result':result}
    return render(request, 'myadmin/feedback.html',context)

def delete_fed(request,id):
    result = Feedback.objects.get(pk=id)
    result.delete()
    return redirect('/myadmin/feedback')

def clients(request):
    context = {}
    return render(request, 'myadmin/clients.html',context)

def all_dates(request):
    result = Hearing.objects.all()
    context = {'result':result}
    return render(request,'myadmin/all_dates.html',context)


def read_appointment(request):
    result = Appointment.objects.all()
    context = {'result':result}
    return render(request,'myadmin/read_appointment.html',context)


def accept_ap(request,id):
    context = {'a_id':id}
    return render(request,'myadmin/accept_ap.html',context)


def store_ap(request,id):
    myremarks = request.POST['remarks']
    mydate  = request.POST['date']
    mytime  = request.POST['time']
    Appointment.objects.update_or_create(pk=id,defaults={'status':'Accepted','remarks':myremarks,'date':mydate,'time':mytime})
    return redirect('/myadmin/read_appointment/')


def reject_ap(request):
    context = {}
    return render(request,'myadmin/reject_ap.html',context)


def reject_reason(request):
    myremarks = request.POST['remarks']


    Appointment.objects.update_or_create(pk=id,defaults={'status':'Rejected','remarks':myremarks})
    return redirect('/myadmin/read_appointment/')


def search_case(request):
    result = Case.objects.all()
    context = {'result': result}
    return render(request,'myadmin/search_case.html',context)


def change_password(request):
    context = {}
    return render(request,'myadmin/change_password.html',context)

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
            return redirect('/myadmin/login')
        else:
            messages.success(request, 'Invalid Password Try Again')
            return redirect('/myadmin/change_password/')     
    else:
         messages.success(request, 'Miss Match Password')


