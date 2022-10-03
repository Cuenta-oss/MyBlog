from django.db import models
from django.contrib.auth import get_user_model
from appStore.models import products
from django.db.models import F, Sum, FloatField

User = get_user_model()

class pedido(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.lineapedido_set_aggregate(
            total = Sum(F("priceProduct") * F("cantidad"), Output_field = FloatField)
        )["total"]
    
    class Meta:
        db_table = 'pedido'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class lineapedido(models.Model):
    cantidad = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(pedido, on_delete=models.CASCADE)
    
    def __str__(self):
        return "cantidad {} producto {}".format(self.cantidad, self.product_id.nameProduct)

    class Meta:
        db_table = 'lineaPedido'
        verbose_name = 'lineaPedido'
        verbose_name_plural = 'lineaPedidos'
        ordering = ['id']