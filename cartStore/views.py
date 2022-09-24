from django.shortcuts import render
from .carro import car_store
from appStore.models import products
from django.shortcuts import redirect

# Create your views here.

def add_product(request, id_product):
    carro = car_store(request)
    product = products.objects.get(id = id_product)
    carro.add_to_cart(product = product)
    
    return redirect("store")

def delete_product_all(request, id_product):
    carro = car_store(request)
    product = products.objects.get(id = id_product)
    carro.delete_products_all(product = product)
    
    return redirect("store")

def delete_product_amount(request, id_product):
    carro = car_store(request)
    product = products.objects.get(id = id_product)
    carro.delete_product_amount(product)
    
    return redirect("store")

def empty_cart(request):
    carro = car_store(request)
    carro.empty_cart()
    return redirect("store")
