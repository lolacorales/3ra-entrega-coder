from django import forms
from app_coder.models import Libro, Critico, Reseña

class NuevoLibro(forms.Form):
    titulo = forms.CharField(max_length=100)
    año = forms.IntegerField()
    autor = forms.CharField(max_length=100)


class NuevoCritico(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()

class NuevaReseña(forms.Form):
    texto = forms.CharField()
    libro = forms.ModelChoiceField(queryset=Libro.objects.all())
    critico = forms.ModelChoiceField(queryset=Critico.objects.all())
