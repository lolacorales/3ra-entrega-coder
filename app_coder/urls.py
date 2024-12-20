from django.contrib import admin
from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('inicio/', inicio, name="Inicio"),
    path ('nuevo_libro/', nuevo_libro, name="Nuevo Libro"),
    path ('nuevo_critico/', nuevo_critico, name="Nuevo Critico"),
    path ('nueva_reseña/', nueva_reseña, name="Nueva Reseña"),
    path ('eliminar_reseña/<int:pk>', eliminar_reseña, name="eliminar_reseña"),
    path('editar_reseña/<int:pk>', editar_reseña, name="editar_reseña"),
    path ('eliminar_libro/<int:pk>', eliminar_libro, name="eliminar_libro"),
    path('editar_libro/<int:pk>', editar_libro, name="editar_libro"),
    path('buscar_libro/', buscar_libro, name="buscar_libro"),

]