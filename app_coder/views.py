from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render


def inicio(request):
    return render(request, 'app_coder/inicio.html')

def nuevo_libro(request):
    return render(request, 'app_coder/nuevo_libro.html')

def nuevo_critico(request):
    return render(request, 'app_coder/nuevo_critico.html')

def nueva_reseña(request):
    return render(request, 'app_coder/nueva_reseña.html')
