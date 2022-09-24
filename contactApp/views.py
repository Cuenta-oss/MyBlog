from django.shortcuts import render, redirect
from .forms import formContact
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.


def contact(request):

    form_contact = formContact()

    if request.method == 'POST':
        form_contact = formContact(data=request.POST)
        if form_contact.is_valid():
            nombre = request.POST.get('nameUser')
            correo = request.POST.get('emailUser')
            description = request.POST.get('descriptionUser')

            correo = EmailMessage(
                "Message received",
                "El usuario {} con correo {} dice lo siguiente\n\n {} \n".format(
                    nombre, correo, description),
                "",
                [settings.EMAIL_HOST_USER],
                reply_to=[correo]
            )
            try:
                correo.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?novalid')
    context = {
        'var': form_contact,
    }
    return render(request, 'contactApp/contact.html', context)
