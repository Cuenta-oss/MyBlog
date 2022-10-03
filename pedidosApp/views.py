from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import User, lineapedido, pedido
from cartStore.carro import car_store
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


@login_required(login_url="/auth_user/log_in")
def procesarPedidos(request):
    proPedidos = pedido.objects.create(username = request.user)
    cart = car_store(request)
    lista_pedidos = list()
    for key, value in cart.carro.items():
        lista_pedidos.append(lineapedido(
            id_product=key,
            amount=value["amount"],
            user=request.user,
            proPedidos=proPedidos
        ))
    lineapedido.objects.bulk_create(lista_pedidos)

    send_mail(
        proPedidos=proPedidos,
        lineapedido=lineapedido,
        nombre_user=request.username,
        email_user=request.mail
    )

    messages.success(request, "Se creo un pedido nuevo")

    return redirect("../store")


def send_mails(**kwargs):
    asunto = "Gracias por comprar"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("proPedidos "),
        "lineapedido": kwargs.get("lineapedido"),
        "nombre_user": kwargs.get("nombre_user")

    })

    sending_message = strip_tags(mensaje)
    mail_from = "scriptexe462@gmail.com"
    """ mail_to = kwargs.get("email_user") """
    mail_to = "ejmenrique97@gmail.com"

    send_mail(
        asunto,
        sending_message,
        mail_from,
        [mail_to],
        html_message=mensaje
    )
