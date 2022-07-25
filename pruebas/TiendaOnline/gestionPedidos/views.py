from django.http import HttpResponse
from django.shortcuts import render
from gestionPedidos.models import Articulos
from django.conf import settings
from django.core.mail import send_mail
from gestionPedidos.forms import formulario_contacto

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    producto_buscado = request.GET["producto"]

    if(producto_buscado):
        if(len(producto_buscado) <= 20):
            articulos = Articulos.objects.filter(nombre__icontains=producto_buscado)

            return render(request, "resultados_busqueda.html", {"articulos": articulos, "query": producto_buscado})
        else:
            return HttpResponse("El texto introducido es demasiado largo.")
    else:
        return HttpResponse("No has introducido nada.")

def obtener_contactos(request):
    if(request.method == "POST"):
        #asunto = request.POST["asunto"]
        #email  = request.POST["email"]
        #mensaje = request.POST["mensaje"]+ " " + email
        #email_origen = settings.EMAIL_HOST_USER

        #lista_contenedora = ["mmontalbapavez@gmail.com"]

        #send_mail(asunto, mensaje, email_origen, lista_contenedora, False)
        #return render(request, "gracias.html")

        formulario = formulario_contacto(request.POST)
        if(formulario.is_valid()):
            informacion_formulario = formulario.cleaned_data
            send_mail(informacion_formulario["asunto"],
                      informacion_formulario["mensaje"],
                      informacion_formulario.get("email",""),
                      ["mmontalbapavez@gmail.com"]
                      )
            
            return render(request, "gracias.html")
        
    else:
        formulario = formulario_contacto()

    return render(request, "formulario_contacto.html", {"form": formulario})