from django.conf.urls import url,include
from django.contrib import admin
from paintermodule.views import UploadView,PainterView,UpdatePainter,PaintListView
from paintermodule import views
#from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
	
    url(r'^painter/',PainterView.as_view(),name='painter'),
    url(r'^upload/',UploadView.as_view(),name='upload'),
    url(r'^update/',UpdatePainter.as_view(),name='update'),
    url(r'^pintlist/',PaintListView.as_view(),name='pintlist')
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
