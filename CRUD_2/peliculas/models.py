from django.db import models

# Create your models here.
class Pelicula(models.Model):
    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=50)
    portada     = models.ImageField(upload_to="peliculas/portadas/", null=True, verbose_name="Imagen")
    descripcion = models.TextField(null=True, blank=True)
    genero      = models.TextField(null=True, blank=True)
    director    = models.CharField(max_length=30)

    def delete(self, using=None, keep_parents=False):
        self.portada.storage.delete(self.portada.name)
        super().delete()

    def __str__(self):
        fila = "ID = %i  -  NOMBRE = '%s'   -   DIRECTOR = %s"%(self.id, self.nombre, self.director) 
        return fila
    
    class Meta:
        verbose_name_plural = "Peliculas"