# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Painter(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	rgtrtype=(('Painter','Painter'),('Buyer','Buyer'))
	Adress=models.CharField(max_length=80)
	Nationality=models.CharField(max_length=10)
	Phone =models.IntegerField()
	Registration_type=models.CharField(max_length=23,choices=rgtrtype)
	created_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.Adress
