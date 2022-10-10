from django.contrib import admin
from . import models

class LibroAdmin(admin.ModelAdmin):
    list_filter = ("autor__nombre", "categoria")

# Register your models here.
admin.site.register(models.Autor)
admin.site.register(models.Categoria)
admin.site.register(models.Libro, LibroAdmin)
admin.site.register(models.Stock)
admin.site.register(models.Carrito)