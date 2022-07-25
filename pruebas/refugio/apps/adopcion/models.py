from django.db import models

# Create your models here.
class Persona(models.Model):
    folio     = models.CharField(max_length=10, primary_key=True)
    nombre    = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad      = models.IntegerField()
    telefono  = models.CharField(max_length=12)
    email     = models.EmailField()
    domicilio = models.TextField()