from django.contrib import admin

from app_coder.models import Libro, Critico, Reseña

admin.site.register(Libro)
admin.site.register(Critico)
admin.site.register(Reseña)