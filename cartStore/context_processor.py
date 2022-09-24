
def total_import(request):
    total = 0
    if request.user.is_authenticated:
        if 'carro' in request.session:
            for key, value in request.session["carro"].items():
                total = total + (float(value['price_product']))
    return {'total_import': total}
