#-*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Estados(models.Model):
    pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais', blank=True, null=True)
    estado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estados'

    def __str__(self):
        return '%s' % (self.estado)


class Pais(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    nombre = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'

    def __str__(self):
        return '%s' % (self.nombre)
