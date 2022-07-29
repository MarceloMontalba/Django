from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from .forms import ImagenFormulario, PeliculaFormulario
import peliculas

# Create your views here.
def mostrar_inicio(request):
    if request.method == "POST":
        buscar = request.POST.get("buscar_pelicula")
        
        if buscar != None:
            peliculas = models.Pelicula.objects.filter(nombre__icontains=buscar)
            return render(request, "secciones/index.html",{"peliculas": peliculas})

    peliculas = models.Pelicula.objects.all()
    return render(request, "secciones/index.html", {"peliculas": peliculas});

def mostrar_detalles(request, id, editar):
    pelicula = models.Pelicula.objects.get(id=id)
    formulario = PeliculaFormulario(request.POST or None, request.FILES or None, instance=pelicula)

    if formulario.is_valid() and request.method == "POST":
        formulario.save()

        return redirect("../../detalles/%i/0"%id)

    renderiza = {"pelicula": pelicula, 
                 "editar": editar,
                 "formulario": formulario}

    return render(request, "funciones/ver_detalles.html", renderiza)

def crear_pelicula(request):
    formulario = PeliculaFormulario(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()

        return redirect("inicio")

    return render(request, "funciones/crear_pelicula.html", {"formulario": formulario})

def eliminar_pelicula(request, id):
    pelicula = models.Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect("inicio")