from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name="inicio"),
    path('AgregarNota/', views.AgregarNota, name="agregar-nota"),
    path('detalles/<int:id>/', views.Detalles, name="detalles"),
    path('eliminar/<int:id>/', views.Eliminar, name="borrar"),
]