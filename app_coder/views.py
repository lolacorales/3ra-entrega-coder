from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from app_coder.forms import NuevoLibro
from app_coder.models import *

def inicio(request):
    reseñas = reseña.objects.all ()
    print (reseñas)    
    return render(request, 'app_coder/inicio.html')


def nuevo_libro(request):
    if request.method == "POST":
        formulario = NuevoLibro(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            nuevolibro = libro (titulo = informacion['titulo'], año = informacion ['año'], autor = informacion ['autor'])
            nuevolibro.save()
            return inicio(request)
    else:
        formulario = NuevoLibro()
    return render(request, 'app_coder/nuevo_libro.html', {"formulario": formulario})

def nuevo_critico(request):
    return render(request, 'app_coder/nuevo_critico.html')

def nueva_reseña(request):
    return render(request, 'app_coder/nueva_reseña.html')
