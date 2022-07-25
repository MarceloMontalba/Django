from django.contrib import admin
from encuestas.models import Encuesta, Opcion

#Cambios a los distintos titulos de la aplicación 
#en el administrador
admin.site.site_header = "Administrador de Encuestas :D"

class opcion_inline(admin.TabularInline):
    model = Opcion

class administrador_encuesta(admin.ModelAdmin):
    list_display  = ("nombre","apellido","fecha_nacimiento")
    search_fields = ("nombre",)
    list_filter   = ("nombre","apellido","fecha_nacimiento")
    fields        = ("nombre","apellido","fecha_nacimiento")
    date_hierarchy = ("fecha_nacimiento")
    inlines       = [opcion_inline,]

class administrador_opcion(admin.ModelAdmin):
    list_display  = ("asegurado","trabajando")
    search_fields = ("asegurado", "trabajando")
    list_filter   = ("asegurado","trabajando")
    
# Register your models here.
admin.site.register(Encuesta, administrador_encuesta)
admin.site.register(Opcion, administrador_opcion)