from django.urls import path
from . import views

urlpatterns = [
    path("", views.loguearse, name="loguearse"),
    path("registrarse", views.registrarse, name="registrarse"),
    path("inicio/<str:usuario>", views.mostrar_inicio, name="inicio"),
    path("cerrar", views.cerrar_sesion, name="cerrar"),
]