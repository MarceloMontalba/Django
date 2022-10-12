from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from . import models

# Create your views here.
def Inicio(request):
    notas = models.Nota.objects.all().order_by('-actualizado')
    if(request.method=="POST"):
        buscador = request.POST.get("buscador")
        if buscador != "":
            notas = models.Nota.objects.filter(titulo__icontains=buscador).order_by('-actualizado')

    informacion = {"notas": notas}
    return render(request, "inicio.html", informacion)

def AgregarNota(request):
    if request.method == "POST":
        nueva_nota = models.Nota(titulo=request.POST["titulo"], contenido=request.POST["contenido"])
        nueva_nota.save()
        return HttpResponseRedirect(reverse("inicio"))

    return render(request, "agregar.html")

def Detalles(request, id):
    nota = models.Nota.objects.get(id=id)
    if(request.method == "POST"):
        nota.titulo    = request.POST["titulo"]
        nota.contenido = request.POST["contenido"]
        nota.save()

        return HttpResponseRedirect(reverse("inicio"))

    informacion = {"nota": nota}
    return render(request, "detalles.html", informacion)

def Eliminar(request, id):
    nota = models.Nota.objects.get(id=id)
    nota.delete()
    return HttpResponseRedirect(reverse("inicio"))