# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View,DeleteView
from django.contrib.auth.models import User
from login.models import Painter
from paintermodule.models import Painter 
# Create your views here.
class AdminHomeView(View):
	model=Painter
	template_name='adminhome.html'
	def get(self,request):
		object_list=User.objects.all()
		paintr=Painter.objects.all()
		context={
			'object_list':object_list,
			'paintr':paintr
		}
		return render(request,self.template_name,context)

class AdminListView(View):
	model=Painter
	template_name='adminhome.html'
	def get(self,request):
		img=Painter.objects.all()
		context={
			'img':img
		}		
class AdminDeleteView(DeleteView):
	template_name="admindelete.html"
	model = User
	success_url='/adminhome/'
