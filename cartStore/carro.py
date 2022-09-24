class car_store:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")

        if not carro:
            carro = self.session["carro"] = {}
        #else:
        self.carro = carro

    def add_to_cart(self, product):
        if (str(product.id) not in self.carro.keys()):
            self.carro[product.id] = {
                'id_product': product.id,
                'name_product': product.nameProduct,
                'price_product': str(product.priceProduct),
                'amount': 1,
                'image_product': product.imageProduct.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(product.id):
                    value['amount'] += 1
                    value['price_product'] = float(value['price_product']) + product.priceProduct 
                    break
        self.save_all()

    def save_all(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def delete_products_all(self, product):
        product.id = str(product.id)
        if product.id in self.carro:
            del self.carro[product.id]
            self.save_all()

    def delete_product_amount(self, product):
        for key, value in self.carro.items():
            if key == str(product.id):
                value['amount'] = value['amount'] - 1
                value['price_product'] = float(value['price_product']) - product.priceProduct
                if value['amount'] < 1:
                    self.delete_products_all(product)
                break
        self.save_all()
        
    def empty_cart(self):
        carro = self.session["carro"] = {}
        self.session.modified = True        
