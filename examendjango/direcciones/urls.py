# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    #--------------------------------------------------------------------------
    url(r'^usuarios', views.Usuarios.as_view(), name="us"),
    url(r'^crea-u/', views.CreateUsuarios.as_view(), name="cus"),
    url(r'^update-u/', views.UpdateUsuarios.as_view(), name="uus"),
    url(r'^delete-u/', views.DeleteUsuarios.as_view(), name="dus"),
    url(r'^pass/', views.UpdatePassword.as_view(), name="cpass"),
    #--------------------------------------------------------------------------
    url(r'^direcciones/', views.Direcciones.as_view(), name="ad"),
    url(r'^crea-d/', views.CreateDireccion.as_view(), name="cadd"),
    url(r'^update-d/', views.UpdateDireccion.as_view(), name="uadd"),
    url(r'^delete-d/', views.DeleteDireccion.as_view(), name="dadd"),
    #--------------------------------------------------------------------------
    url(r'^salir/', views.salir, name="logout"),
]