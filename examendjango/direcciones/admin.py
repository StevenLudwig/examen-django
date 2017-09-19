# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models


class DireccionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'calle',
        'num_calle',
        'num_int',
        'municipio',
        'colonia',
        'estado',
        'pais',)
    search_fields = ('user',)

admin.site.register(models.Direccion, DireccionAdmin)