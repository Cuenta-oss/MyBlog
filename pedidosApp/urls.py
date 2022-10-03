from django.urls import path
from . import views

urlpatterns = [
    path("", views.procesarPedidos, name="procesar_pedido")
]