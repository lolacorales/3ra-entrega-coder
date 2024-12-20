from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import redirect, render, get_object_or_404
from app_coder.forms import FormularioLibro, FormularioReseña, FormularioCritico
from app_coder.models import *

def inicio(request):
        reseñas = Reseña.objects.all()
        contexto = {"reseñas":reseñas}
        return render(request, "app_coder/inicio.html", contexto)
    

#####################  CRUD RESEÑAS  ###################################
def inicio(request):
    query = request.GET.get('q')
    if query:
        reseñas = Reseña.objects.filter(libro__titulo__icontains=query)
    else:
        reseñas = Reseña.objects.all()
    context = {
        "reseñas": reseñas,
        "query": query,
        "no_results": not reseñas.exists() if query else False
    }
    return render(request, "app_coder/inicio.html", context)

def nueva_reseña (request):
    if request.method == 'POST':
        formulario_reseña = FormularioReseña(request.POST)
        if formulario_reseña.is_valid():
            formulario_reseña.save()
            return redirect ("Inicio")
    else:
        formulario_reseña = FormularioReseña()
        return render(request, 'app_coder/nueva_reseña.html', {"formulario_reseña": formulario_reseña})

def eliminar_reseña(request, pk):
    reseña = Reseña.objects.get(pk=pk)
    reseña.delete ()
    return redirect("Inicio")

def editar_reseña(request, pk):
    reseña = get_object_or_404(Reseña, pk=pk)  
    if request.method == "POST":
        formulario = FormularioReseña(request.POST, instance=reseña)  
        if formulario.is_valid():
            formulario.save()  
            return redirect("Inicio")
    else:
        formulario = FormularioReseña(instance=reseña)  
    return render(request, "app_coder/editar_reseña.html", {"formulario": formulario})



############### CRUD LIBROS ###############

def nuevo_libro(request):
    if request.method == 'POST':
        formulario_libro = FormularioLibro(request.POST)
        if formulario_libro.is_valid():
            formulario_libro.save()
            return redirect ("Inicio")
    else:
        formulario_libro = FormularioLibro()
    return render(request, 'app_coder/nuevo_libro.html', {"formulario_libro": formulario_libro})


def buscar_libro(request):
    query = request.GET.get('q')
    if query:
        libros = Libro.objects.filter(titulo__icontains=query)
    else:
        libros = Libro.objects.all()
    context = {
        "libros": libros,
        "query": query,
        "no_results": not libros.exists() if query else False
    }
    return render(request, "app_coder/inicio.html", context)

def eliminar_libro(request, pk):
    libro = Libro.objects.get(pk=pk)
    libro.delete ()
    return redirect("Inicio")

def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)  
    if request.method == "POST":
        formulario_libro = FormularioLibro(request.POST, instance=libro)  
        if formulario_libro.is_valid():
            formulario_libro.save()  
            return redirect("Inicio")
    else:
        formulario_libro = FormularioReseña(instance=libro)  
    return render(request, "app_coder/editar_libro.html", {"formulario_libro": formulario_libro})


############### CRUD CRITICOS ############### 

def nuevo_critico (request):
    if request.method == 'POST':
        formulario_critico = FormularioCritico(request.POST)
        if formulario_critico.is_valid():
            formulario_critico.save()
            return redirect ("Inicio")
    else:
        formulario_critico = FormularioCritico()
    return render(request, 'app_coder/nuevo_critico.html', {"formulario_critico": formulario_critico})
