from django.db import models

# Create your models here.

class Services(models.Model):
    titulo=models.CharField(max_length=60)
    descripcion=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to='Services')

    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
    
    def __str__(self):
        return self.titulo