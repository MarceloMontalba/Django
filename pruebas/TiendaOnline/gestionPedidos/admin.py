from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

class clientes_admin(admin.ModelAdmin):
    list_display = ("id", "nombre", "direccion", "telefono")
    search_fields = ("nombre", "telefono")

class articulos_admin(admin.ModelAdmin):
    list_display = ("nombre","seccion","precio")
    list_filter  = ("seccion",)

class pedidos_admin(admin.ModelAdmin):
    list_display = ("numero","fecha")
    list_filter  = ("fecha",) 
    date_hierarchy = "fecha"

admin.site.register(Clientes, clientes_admin)
admin.site.register(Articulos, articulos_admin)
admin.site.register(Pedidos, pedidos_admin)