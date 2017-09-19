# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from .db import Estados, Pais


class Direccion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calle = models.CharField(max_length=30)
    num_calle = models.IntegerField('Numero de Calle')
    num_int = models.CharField('Numero interior', max_length=5, default="N/A")
    municipio = models.CharField(max_length=100)
    colonia = models.CharField(max_length=100)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (
            self.user,
            self.calle,
            self.num_calle,
            self.num_int,
            self.municipio,
            self.colonia,
            self.estado,
            self.pais)