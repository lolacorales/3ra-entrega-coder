from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import redirect, render, get_object_or_404
from app_coder.forms import NuevoLibro, NuevaReseña, NuevoCritico
from app_coder.models import *

def inicio(request):
        reseñas = Reseña.objects.all()
        contexto = {"reseñas":reseñas}
        return render(request, "app_coder/inicio.html", contexto)
    

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



def nuevo_libro(request):
    if request.method == "POST":
        formulario = NuevoLibro(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            nuevolibro = Libro (titulo = informacion['titulo'], año = informacion ['año'], autor = informacion ['autor'])
            nuevolibro.save()
            return inicio(request)
    else:
        formulario = NuevoLibro()
    return render(request, 'app_coder/nuevo_libro.html', {"formulario": formulario})

def nuevo_critico(request):
    if request.method == "POST":
        formulario_critico = NuevoCritico(request.POST)
        print(formulario_critico)
        if formulario_critico.is_valid:
            informacion_critico = formulario_critico.cleaned_data
            nuevocritico = Critico (nombre = informacion_critico['nombre'], email = informacion_critico ['email'])
            nuevocritico.save()
            return inicio(request)
    else:
        formulario_critico = NuevoCritico()
    return render(request, 'app_coder/nuevo_critico.html', {"formulario_critico": formulario_critico})

def nueva_reseña(request):
    if request.method == "POST":
        formulario_reseña = NuevaReseña(request.POST)
        print(formulario_reseña)
        if formulario_reseña.is_valid:
            informacion_reseña = formulario_reseña.cleaned_data
            nuevareseña = Reseña(texto = informacion_reseña['texto'], libro = informacion_reseña ['libro'], critico = informacion_reseña ['critico'])
            nuevareseña.save()
            return inicio(request)
    else:
        formulario_reseña = NuevaReseña()
    return render(request, 'app_coder/nueva_reseña.html', {"formulario_reseña": formulario_reseña})

def eliminar_reseña(request, pk):
    reseña = Reseña.objects.get(pk=pk)
    reseña.delete ()
    return redirect("Inicio")


# def editar_reseña(request, pk):
#     reseña = Reseña.objects.get(pk=pk)
#     if request.method == "POST":
#         reseña_editada = NuevaReseña(request.POST)
#         if reseña_editada.is_valid():
#                 info_limpia=reseña_editada.cleaned_data
#                 reseña.texto=info_limpia ["texto"]
#                 reseña.libro=info_limpia ["libro"]
#                 reseña.critico=info_limpia ["critico"]
#                 reseña.save()
#         return redirect ("inicio")
#     else:
#         reseña_editada = nueva_reseña(initial = {"texto":reseña.texto, "libro":reseña.libro, "critico":reseña.critico})
#         return render (request, "app_coder/editar_resena.html",{"reseña_editada":reseña_editada})
    

def editar_reseña(request, pk):
    reseña = get_object_or_404(Reseña, pk=pk)
    
    if request.method == "POST":
        reseña_editada = NuevaReseña(request.POST, instance=reseña)
        
        if reseña_editada.is_valid():
                reseña_editada.save()
                return redirect ("inicio")
    else:
        reseña_editada = nueva_reseña(instance = reseña)
        return render (request, "app_coder/editar_resena.html",{"reseña_editada":reseña_editada})