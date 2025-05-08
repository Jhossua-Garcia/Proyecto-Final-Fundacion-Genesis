from django.contrib import admin
from .models import Carrito,Carrito_Item

# Registrar el modelo Carrito y Carrito_Item en el admin de Django

class CarritoAdmin(admin.ModelAdmin):
    list_display=('id_carrito','fecha_agregado')

class CarritoItemAdmin(admin.ModelAdmin):
    list_display=('producto','carrito','cantidad','is_active')
    
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Carrito_Item,CarritoItemAdmin)

