from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Libros, name='libros'),
    path('categoria/<int:id_categoria>/', views.LibrosCategoria, name='libros_categoria'),
    path('libro/<int:id_libro>/', views.LibroDetalles, name="libro_detalles"),
]