from atexit import register
from django.contrib import admin
from .models import lineapedido, pedido
# Register your models here.

admin.site.register(lineapedido)
admin.site.register(pedido)