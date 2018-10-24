from django.conf.urls import include,url
from django.contrib import admin
from login.views import HomeView,RegisterView,DiscocerView
from login import views

urlpatterns=[
    url(r'^home/',HomeView.as_view(),name='home'),

    url(r'^login/$', views.login, name='login'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/',RegisterView.as_view(),name='register'),
]
