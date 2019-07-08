from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
class Cliente( models.Model ):
    tipo = (('Arrendatario','Arrendatario'),
           ('Cliente','Cliente'))
    rut = models.CharField(primary_key = True, max_length = 50 )
    nombre = models.CharField(max_length = 50, null=False, blank=False )
    telefono = models.CharField ( max_length=9, null=False, blank=False )
    correo = models.CharField(max_length=2550, blank=True )
    direccion = models.CharField(max_length=2550, blank=True )
    num_tarj = models.CharField(max_length=2550, blank=True )
    banco = models.CharField(max_length=2550, blank=True )
    tipo  = models.CharField(null=True, default='Cliente',choices=tipo,max_length=30)
    patente = models.CharField(max_length=2550, blank=True )
    marca = models.CharField(max_length=2550, blank=True )
    modelo = models.CharField(max_length=2550, blank=True )
    año = models.CharField(max_length=2550, blank=True)

    def __str__ ( self ):
        return self.nombre


class Estacionamiento (models.Model):
    dueño = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    direccion = models.CharField(max_length=2550, blank=True,null=True)
    descripcion = models.CharField(max_length=2550, blank=True,null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    

    def __str__ (self):
        return self.direccion

        
