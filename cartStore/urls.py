from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add_product/<int:id_product>", views.add_product, name="agregar"),
    path("delete_product_all/<int:id_product>", views.delete_product_all, name='delete_product_all'),
    path("delete_product_amount/<int:id_product>", views.delete_product_amount, name='delete_product_amount'),
    path("empty_cart/<int:id_product>", views.empty_cart, name='empty_cart'),
]
