from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.
class Nota(models.Model):
    id          = models.AutoField(primary_key=True)
    titulo      = models.CharField(max_length=50)
    contenido   = models.TextField()
    actualizado = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "Notas"
         