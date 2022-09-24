from distutils.command.upload import upload
from tabnanny import verbose
from venv import create
from django.db import models

# Create your models here.

class servicio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        
    def __str__(self):
        return self.title