# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Painter(models.Model):
	painting_name=models.CharField(max_length=40)
	painting_type=models.CharField(max_length=30)
	painting_size=models.IntegerField(default=40)
	painter_name=models.CharField(max_length=80)
	painting_prize=models.FloatField()
	painting_picture=models.ImageField(upload_to='media/pic')
	created_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.painting_name
	
