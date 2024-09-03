from django.db import models
from datetime import date
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Contact(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.CharField(max_length=80)
    contact  = models.BigIntegerField()
    message  = models.TextField()
    date     = models.DateField(default=date.today())

    class Meta:
        db_table = 'contact'

class Feedback(models.Model):
    rating = models.CharField(max_length=50)
    comment  = models.TextField()
    user     = models.OneToOneField(User,on_delete=models.CASCADE)
    date     = models.DateField(default=date.today())

    class Meta:
        db_table = 'feedback'


class Appointment(models.Model):
    subject  = models.CharField(max_length=50)
    description  = models.TextField()
    status  = models.CharField(max_length=30,default='pending')
    remarks = models.CharField(max_length=100,default='')
    date     = models.DateField(null=True, blank=True)
    time    =  models.TimeField(null=True, blank=True)
    user     = models.ForeignKey(User,on_delete=models.CASCADE,default='')


    class Meta:
        db_table = 'appointment'








