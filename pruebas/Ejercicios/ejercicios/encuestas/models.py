from pyexpat import model
from django.db import models

# Create your models here.
class Encuesta(models.Model):
    nombre           = models.CharField(max_length=30)
    apellido         = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(blank = True, null = True)

    class Meta:
        verbose_name_plural ="Encuestas"

class Opcion(models.Model):
    asegurado  = models.BooleanField()
    trabajando = models.BooleanField()
    encuestado = models.ForeignKey(Encuesta, on_delete= models.PROTECT)

    class Meta: 
        verbose_name_plural = "Opciones"