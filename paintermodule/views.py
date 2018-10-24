# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,FormView,TemplateView,ListView
from paintermodule.models import Painter
from paintermodule.forms import PainterForm
# sCreate your views here.
class PainterView(TemplateView):
	"""docstring for """
	template_name='painter.html'
	
	#def get(self,request):
		#if request.user.is_staff:
		#	return render(request,self.template_name)
		#else:
		#	return redirect('/painter/')
class UploadView(CreateView):
	"""docstring for """
	template_name='uploaddetails.html'
	form_class=PainterForm
	model=Painter
	success_url='success'

class UpdatePainter(UpdateView):
	model=Painter
	template_name='painter.html'
	form_class=PainterForm

class PaintListView(ListView):
	"""docstring for CuVehicleListView"""
	template_name='painter.html'
	def get_queryset(self):
		logged_user=self.request.user
		print(logged_user)
		queryset = PainterModel.objects.filter(user=logged_user)
		return queryset
