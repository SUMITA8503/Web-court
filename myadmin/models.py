from django.db import models
from datetime import date
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class State(models.Model):
    state_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'state'


class City(models.Model):
    city_name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'

class Area(models.Model):
    area_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'area'

class Staff(models.Model):
    user    = models.OneToOneField(User,on_delete=models.CASCADE)
    gender   = models.CharField(max_length=30) 
    contact  = models.BigIntegerField()
    address  = models.CharField(max_length=80)
    image    = models.CharField(max_length=255)
    city     = models.ForeignKey(City, on_delete=models.CASCADE)
    area     = models.ForeignKey(Area, on_delete=models.CASCADE)
    date     = models.DateField(default=date.today())

    class Meta:
        db_table = 'staff'


class Client(models.Model):
    user    = models.OneToOneField(User,on_delete=models.CASCADE)
    gender   = models.CharField(max_length=30) 
    contact  = models.BigIntegerField()
    address  = models.CharField(max_length=80)
    image    = models.CharField(max_length=255)
    city     = models.ForeignKey(City, on_delete=models.CASCADE)
    area     = models.ForeignKey(Area, on_delete=models.CASCADE)
    date     = models.DateField(default=date.today())

    class Meta:
        db_table = 'client'


class Case(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    crimetype = models.CharField(max_length=30)
    fir_date = models.DateField()
    fir_station = models.CharField(max_length=30)
    fir_copy = models.CharField(max_length=255)
    status  = models.CharField(max_length=30,default='running')
    remarks = models.CharField(max_length=100,default='')
    city     = models.ForeignKey(City, on_delete=models.CASCADE)
    area     = models.ForeignKey(Area, on_delete=models.CASCADE)
    client   = models.ForeignKey(Client, on_delete=models.CASCADE)
    staff    = models.ForeignKey(Staff, on_delete=models.CASCADE)

    class Meta:
        db_table = 'case'


