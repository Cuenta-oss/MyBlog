from django.contrib import admin
from .models import servicio
# Register your models here.

class servicioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'imagen', 'created', 'updated')
    list_display_links = ('title', 'description', 'imagen', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'description', 'imagen')
    list_per_page = 25
    readonly_fields = ('created', 'updated')
admin.site.register(servicio, servicioAdmin)
