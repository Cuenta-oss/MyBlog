from django.shortcuts import render
from appStore.models import productCategory, products

# Create your views here.


def store(request):
    varStore = products.objects.all()

    context = {
        'varStore': varStore
    }
    
    return render(request, 'store.html', context)
