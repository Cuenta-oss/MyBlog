from django.shortcuts import render
from appServices.models import servicio
# Create your views here.


def services(request):
    varService = servicio.objects.all()
    context = {
        'services': varService
    }
    return render(request, 'appServices/services.html', context)
