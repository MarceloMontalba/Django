from django import forms
from . import models

class PeliculaFormulario(forms.ModelForm):
    class Meta:
        model = models.Pelicula
        fields = '__all__'

class ImagenFormulario(forms.ModelForm):
    class Meta:
        model = models.Pelicula
        fields = ["portada"]