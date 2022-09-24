from django.contrib import admin
from .models import productCategory, products
# Register your models here.


class productsAdminStore(admin.ModelAdmin):
    list_display = ('nameProduct', 'imageProduct',
                    'statusProduct', 'categories', 'priceProduct', 'created', 'updated')
    list_display_links = ('nameProduct', 'imageProduct',
                          'statusProduct', 'categories', 'priceProduct')
    list_filter = ('nameProduct',)
    search_fields = ('nameProduct',)


admin.site.register(products, productsAdminStore)


class categoryAdminStore(admin.ModelAdmin):
    list_display = ('nameCategory',
                    'created', 'updated')
    list_display_links = ('nameCategory',
                          'created', 'updated')
    list_filter = ('nameCategory',)
    readonly_fields = ('created', 'updated')


admin.site.register(productCategory, categoryAdminStore)
