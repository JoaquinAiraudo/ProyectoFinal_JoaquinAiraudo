from django.db import models
from django.contrib.auth.models import User

# Create your models here.  
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='Blog', null=True, blank=True)
    contenido = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'