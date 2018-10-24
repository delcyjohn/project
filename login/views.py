# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView,FormView,View
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

from login.forms import UserForm
from login.forms import RegisterForm
from login.models import Painter
from django.contrib import messages
from paintermodule.models import Painter

from django.conf import settings
from django.contrib import messages


# Create your views here.
class LoginView(TemplateView):
	template_name='login.html'
@login_required
def home(request):
    return render(request, 'home.html')
class HomeView(TemplateView):
	template_name='homepage.html'

def login(request):
     form =AuthenticationForm()
     if request.user.is_authenticated():
         if request.user.is_superuser:
             return redirect("/adminhome/")# or your url name
         if request.user.is_staff:
             return redirect("/painter/")# or your url name


     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = auth.authenticate(username=username, password=password)

         if user is not None:
             # correct username and password login the user
             auth.login(request, user)
             if request.user.is_superuser:
                 return redirect("/adminhome/")# or your url name
             if request.user.is_staff:
                 return redirect("/painter/")# or your url name

         else:
             messages.error(request, 'Error wrong username/password')
     context = {}
     context['form']=form

     return render(request, 'login.html', context)

@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
     context = {}
     return render(request, 'painter.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
     context = {}
     return render(request, 'adminhome.html', context)

class RegisterView(FormView):
	template_name="regstr.html"
	form_class=UserForm
	model=Painter
	

	def get(self, request, *args, **kwargs):
		self.object=None
		form_class=self.get_form_class()
		user_form = self.get_form(form_class)
		regstr_form=RegisterForm()
		return self.render_to_response(self.get_context_data
		(form1=user_form,form2=regstr_form))

	def post(self, request, *args, **kwargs):
		self.object=None
		form_class=self.get_form_class()
		user_form = self.get_form(form_class)
		regstr_form=RegisterForm(self.request.POST,self.request.FILES)
		if(user_form.is_valid() and regstr_form.is_valid()):
			return self.form_valid(user_form,regstr_form)
		else:
			return self.form_invalid(user_form,regstr_form)
		
	def form_valid(self, user_form, regstr_form):
		self.object = user_form.save()
		self.object.is_staff=True
		self.object.save()
		p = regstr_form.save(commit=False)
		p.user = self.object
		p.save()	

	def form_invalid(self, user_form, regstr_form):
		return self.render_to_response(self.get_context_data(form1=user_form,form2=regstr_form))	

class DiscocerView(View):
	template_name='homepage.html'
	def get(self,request):
		var_img=Painter.object.all()
		context={
			'var_img':var_img
		}
		return render(request,self.template_name,context)


