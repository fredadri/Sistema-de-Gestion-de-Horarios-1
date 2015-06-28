# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.


def cedula_valida(ced):
    if len(ced) == 10:
        valores = [int(ced[x]) * (2 - x % 2) for x in range(9)]
        suma = sum(map(lambda x: x > 9 and x - 9 or x, valores))
    return int(ced[9]) == 10 - int(str(suma)[-1:])

def validacion(ced):
    if not cedula_valida(ced):
        raise ValidationError(u'%s no es un número de cédula válido' % ced)


def validar_numeros(numero):
    try:
        assert isinstance(numero, object)
        num = int(numero)
    except:
        raise ValidationError(u'%s debe ser numero' % numero)


class Estudiante(models.Model):
    PROGRAMA_CHOICES = (
        ('Master Key English', 'Master Key English'),
        ('Master Key English for kids', 'Master Key English for kids'),
        ('Excelentemente', 'Excelentemente'),)
    DURACION_CHOICES = (
        (3, '3 Meses'),
        (6, '6 Meses'),
        (9, '9 Meses'),
        (12, '12 Meses'),
    )

    cedula = models.CharField(u"cédula", max_length=10, primary_key=True, validators=[validacion])
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(u'fecha de nacimiento',blank=True,null=True)
    telefono = models.CharField(u'teléfono',max_length=10, validators=[validar_numeros])
    programa = models.CharField(max_length=30, choices=PROGRAMA_CHOICES)
    email = models.EmailField(u'e-mail')
    costo_programa = models.PositiveSmallIntegerField()
    duracion = models.PositiveIntegerField(choices=DURACION_CHOICES)
    def __unicode__(self):
        return self.nombre + ' ' + self.apellidos

class Ciudad(models.Model):
    nombre = models.CharField(max_length=25)
    def __unicode__(self):
        return self.nombre

class Sede(models.Model):
    nombre_sede = models.CharField(max_length=20)
    ciudad = models.ForeignKey(Ciudad)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    def __unicode__(self):
        return self.nombre_sede


class Contrato(models.Model):
    numero_contrato = models.CharField(max_length=8, primary_key=True)
    numero_factura = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(u'Fecha de nacimiento',blank=True,null=True)
    cedula = models.CharField(u"Cédula", max_length=10, validators=[validacion])
    email = models.EmailField('e-mail')
    direccion_domicilio = models.TextField()
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10)
    empresa = models.CharField(max_length=30)
    cargo = models.CharField(max_length=20)
    direccion_empresa = models.CharField(max_length=30)
    telefono_empresa = models.PositiveIntegerField()
    fecha_creacion = models.DateField(u'Fecha de creación')
    sede = models.ForeignKey(Sede)
    def __unicode__(self):
        return self.numero_contrato + ' ' + self.nombre + ' ' + self.apellidos