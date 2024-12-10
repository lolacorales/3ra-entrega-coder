from django.contrib import admin
from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('inicio/', inicio, name="Inicio"),
    path ('nuevo_libro/', nuevo_libro, name="Nuevo Libro"),
    path ('nuevo_critico/', nuevo_critico, name="Nuevo Critico"),
    path ('nueva_reseña/', nueva_reseña, name="Nueva Reseña")
]