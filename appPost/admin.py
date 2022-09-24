from django.contrib import admin
from .models import categoryTable, postTable
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = ('titlePost', 'descriptionPost', 'author')
    list_filter = ('created', 'updated')
    search_fields = ('titlePost', 'descriptionPost')
    date_hierarchy = 'created'
    ordering = ('created',)
    list_per_page = 25
    readonly_fields = ('created', 'updated')
    
admin.site.register(postTable, postAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('nameCategory',)
    list_filter = ('created', 'updated')
    search_fields = ('nameCategory',)
    date_hierarchy = 'created'
    ordering = ('created',)
    list_per_page = 25
    readonly_fields = ('created', 'updated')
    
    
admin.site.register(categoryTable, categoryAdmin)