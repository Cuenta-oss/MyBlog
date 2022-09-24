from django.db import models

# Create your models here.appStore/models.py


class productCategory(models.Model):
    nameCategory = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'productCategory'
        verbose_name_plural = 'productCategory'

    def __str__(self):
        return self.nameCategory


class products(models.Model):
    nameProduct = models.CharField(max_length=100)
    imageProduct = models.ImageField(upload_to='store')
    statusProduct = models.BooleanField(default=True)
    categories = models.ForeignKey(productCategory, on_delete=models.CASCADE)
    priceProduct = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.nameProduct
