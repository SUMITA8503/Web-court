from django.db import models
from myadmin.models import *

# Create your models here.

class Document(models.Model):
	case    = models.ForeignKey(Case, on_delete=models.CASCADE)
	title   = models.CharField(max_length=30)
	description   = models.TextField()
	evidence = models.CharField(max_length=255)


	class Meta:
		db_table = 'evidence'

class Hearing(models.Model):
	case     = models.ForeignKey(Case, on_delete=models.CASCADE)
	nextdate = models.DateField()
	remarks  = models.TextField()
	status   = models.CharField(max_length=30)
	description = models.TextField(default='')

	class Meta:
		db_table='hearing'

