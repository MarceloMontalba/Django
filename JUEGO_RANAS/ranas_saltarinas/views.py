from django.shortcuts import render

# Create your views here.
def inicio(request):
    datos = {
        "numero_objetos" : range(7)
    }
    return render(request, "index.html", datos)