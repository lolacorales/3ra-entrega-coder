from django.contrib import admin
from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('inicio/', inicio),
    path ('nuevo_libro/', nuevo_libro),
    path ('nuevo_critico/', nuevo_critico),
    path ('nueva_reseña/', nueva_reseña)
]