from django.contrib import admin
from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('inicio/', inicio),
    path ('registro/', registro),
    path ('busqueda/', busqueda),
    path ('nueva_receta/', nueva_receta),

    path ('template1/', template1),
    ]