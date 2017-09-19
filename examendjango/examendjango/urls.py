#-*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    #----------------------------- Log In & Log out ---------------------------
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #----------------------- Direccion ----------------------------------------
    url(r'^app/', include('direcciones.urls'), name="app"),
    #Api DRF ------------------------------------------------------------------
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    #--------------------------------------------------------------------------
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT, }),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)