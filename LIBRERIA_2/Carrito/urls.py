from django.urls import path
from . import views

urlpatterns = [
    path('', views.Carrito, name="carrito"),
    path('EliminarArticulo/<int:id_articulo>/', views.EliminarArticulo, name="eliminar_articulo"),
]