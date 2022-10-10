from django.shortcuts import render
from . import models

#Funcion que convierte los valores en formato de peso chileno
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
def Libros(request):
    #Lista de libros
    libros = {}
    if request.method == "POST":
        buscar = request.POST.get("buscador-libro")
        if(buscar != ''):
            libros = models.Libro.objects.filter(nombre__icontains=buscar)
        else:
            libros = models.Libro.objects.all()
    else:
        libros = models.Libro.objects.all()

    #Lista de todas las categorias
    categorias = models.Categoria.objects.all()

    for libro in libros:
        libro.precio = IncrustaPuntos(libro.precio)

    #Diccionario con informacion
    informacion = {"libros"      : libros,
                    "categorias" : categorias}
    return render(request, 'libros.html', informacion)

def LibrosCategoria(request, id_categoria):
    libros = models.Libro.objects.filter(categoria__id=id_categoria)

     #Lista de todas las categorias
    categorias = models.Categoria.objects.all()

    for libro in libros:
        #Se deja el dinero en formato de peso chileno
        libro.precio = IncrustaPuntos(libro.precio)   
        
    #Diccionario con informacion
    informacion = {"libros"      : libros,
                    "categorias" : categorias}
    return render(request, 'libros.html', informacion)

def LibroDetalles(request, id_libro):
    if(request.method == "POST"):
        libro    = models.Libro.objects.get(id=id_libro)
        cantidad = request.POST.get("cantidad_libros")
        nueva_fila = models.Carrito(libro=libro, cantidad=cantidad)
        nueva_fila.save()

    #Busqueda del libro 
    libro = models.Libro.objects.get(id=id_libro)
    libro.precio = IncrustaPuntos(libro.precio)   
        
    #Stock en tiendas
    stocks = models.Stock.objects.filter(libro__id=id_libro)

    #Diccionario con informacion
    informacion = {"libro": libro,
                   "stocks": stocks}

    return render(request, "libro_detalles.html", informacion)