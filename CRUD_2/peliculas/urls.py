from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.mostrar_inicio, name="inicio"),
    path('detalles/<int:id>/<int:editar>', views.mostrar_detalles, name="detalles"),
    path('crear/', views.crear_pelicula, name="crear"),
    path('eliminar/<int:id>', views.eliminar_pelicula, name="eliminar"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)