from django.conf.urls import url,include
from django.contrib import admin
from adminmodule.views import AdminHomeView,AdminDeleteView
from adminmodule import views
#from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^adminhome/',AdminHomeView.as_view(),name='adminhome'),
    url(r'^adminupdate/(?P<pk>[0-9]+)/$',AdminDeleteView.as_view(),name='adminupdate'),
]
