from django.db import models

# Create your models here.

class Contact(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    asunto = models.CharField(max_length=20)
    mensaje = models.TextField()


