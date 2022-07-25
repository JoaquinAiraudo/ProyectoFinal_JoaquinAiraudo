from tabnanny import verbose
from django.db import models

# Create your models here.

class Presidente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    asume_cargo = models.DateField()
    deja_cargo = models.DateField()
    partido = models.CharField(max_length=60)
    constitucional = models.BooleanField()

    class Meta:
        verbose_name='Presidente'
        verbose_name_plural='Presidentes'
    
    def __str__(self):
        return '%s, %s' %(self.apellido, self.nombre)


class Ministro(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    asume_cargo = models.DateField()
    deja_cargo = models.DateField()
    cartera = models.CharField(max_length=60)

    class Meta:
        verbose_name='Ministro'
        verbose_name_plural='Ministros'
    
    def __str__(self):
        return '%s, %s' %(self.apellido, self.nombre)


class Partido(models.Model):
    nombre = models.CharField(max_length=60)
    fundacion = models.DateField()
    antiguedad = models.IntegerField()

    class Meta:
        verbose_name='Partido'
        verbose_name_plural='Partidos'
    
    def __str__(self):
        return self.nombre