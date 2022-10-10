from django.shortcuts import render
from Libros import models

# Create your views here.
def inicio(request):
    return render(request, "inicio.html")