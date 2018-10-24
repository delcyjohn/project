from django.conf.urls import url,include
from django.contrib import admin
from buyermodule.views import BuyerView,PainterListView
from buyermodule import views


from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
#from django.contrib.auth import views as auth_views
appname="buyermodule"
urlpatterns = [
	
    url(r'^buyer/',BuyerView.as_view(),name='buyer'),
    url(r'^buyerlist/',PainterListView.as_view(),name='buyerlist'),
    url(r'^payment/$', views.payment, name="payment"),
    url(r'^payment/success$', views.payment_success, name="payment_success"),
    url(r'^payment/failure$', views.payment_failure, name="payment_failure")
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)