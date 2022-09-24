from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class categoryTable(models.Model):
    nameCategory = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.nameCategory


class postTable(models.Model):
    titlePost = models.CharField(max_length=100)
    descriptionPost = models.TextField(max_length=200)
    imagenPost = models.ImageField(upload_to='posts')
    # ForeignKey para relacionar con otra tabla de la base de datos y 
    # on_delete=models.CASCADE para que no se pueda borrar el usuario 
    # si se borra el post asociado a este usuario
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # ManyToManyField para relacionar con varias tablas (muchos a muchos)
    categorias = models.ManyToManyField(categoryTable)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titlePost
