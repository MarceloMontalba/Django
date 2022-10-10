from pyexpat import model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from Libros import models
from django.urls import reverse

def IncrustaPuntos(valor):
    valor = str(valor)[::-1]
    valor_auxiliar = ""
    
    contador = 1
    for numero in valor:
        valor_auxiliar+= numero if(contador<4) else "."+numero

        if(contador<4):
            contador+= 1
        else:
            contador = 0

    return valor_auxiliar[::-1]


# Create your views here.
def Carrito(request):
    carrito = models.Carrito.objects.all()

    for articulo in carrito:
        #Se deja el dinero en formato de peso chileno
        articulo.total        = IncrustaPuntos(articulo.libro.precio*articulo.cantidad)
        articulo.libro.precio = IncrustaPuntos(articulo.libro.precio)   

    informacion = {"carrito" : carrito}
    return render(request, "carrito.html", informacion)

def EliminarArticulo(request, id_articulo):
    articulo = models.Carrito.objects.get(id=id_articulo)
    articulo.delete()
    return HttpResponseRedirect(reverse('carrito'))