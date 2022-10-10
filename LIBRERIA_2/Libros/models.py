from django.db import models

# Create your models here.
class Autor(models.Model):
    id     = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta: 
        verbose_name_plural = "Autores"

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
        
    class Meta: 
        verbose_name_plural = "Categorias"

class Libro(models.Model):
    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=50)
    portada     = models.ImageField(upload_to="Libros/portadas", null=True)
    descripcion = models.TextField(null=True, blank=True)
    categoria   = models.ManyToManyField(Categoria)
    autor       = models.ForeignKey(Autor, on_delete=models.CASCADE)
    precio      = models.IntegerField()

    #En caso de eliminarse el libro se elimina tambien la portada
    #del directorio.
    def delete(self, using=None, keep_parents=False):
        self.portada.storage.delete(self.portada.name)
        super().delete()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Libros"

class Stock(models.Model):
    sucursal = models.CharField(max_length=50)
    libro    = models.ForeignKey(Libro, on_delete=models.CASCADE)
    numero_unidades = models.IntegerField()

    class Meta: 
        verbose_name_plural = "Stock"
    
    def __str__(self):
        return "SUCURSAL: "+self.sucursal+"; LIBRO: "+self.libro.nombre+"; NUMERO_UNIDADES: "+str(self.numero_unidades)

class Carrito(models.Model):
    libro    = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return "LIBRO: "+ self.libro.nombre+ ";     CANTIDAD: "+ str(self.cantidad)