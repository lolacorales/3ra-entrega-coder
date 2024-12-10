from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render


def inicio(request):
    return render(request, 'app_coder/index.html')

def registro(request):
    return HttpResponse ("página de registro")

def busqueda(request):
    return HttpResponse ("página de búsqueda de recetas")

def nueva_receta(request):
    return HttpResponse ("nueva receta")



# def mate(request):
#     return HttpResponse ("tomo mate amargo")

# def minombrees(self, nombre):
#     documentodetexto = f"mi nombre es <br> {nombre}"
#     return HttpResponse (documentodetexto)

def template1(request):
    nom = "lola"
    ap = "corales"
    diccionario = {"nombre": nom, "apellido": ap}
    return render(request, 'template1.html', diccionario)


