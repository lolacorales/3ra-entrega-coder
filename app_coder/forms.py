from django import forms
from app_coder.models import Libro, Critico, Reseña

class FormularioLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = "__all__"
        labels = { 
            'Título': 'Ingrese el nombre del libro',
            'Año': 'Ingrese año de publicación',
            'Autor': 'Ingrese autor del libro',
        }
        widgets = {
            "Título": forms.TextInput(attrs={ 
                "class":"form-control", "placeholder":"Ingrese el título del libro"
            },),
            "Año":forms.NumberInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el año de publicación"
            }),
            "Autor": forms.TextInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el autor"
            })
        }

class FormularioCritico(forms.ModelForm):
    class Meta:
        model = Critico
        fields = "__all__"
        labels = { 
            'Nombre': '',
            'Email': '',
            }
        widgets = {
            "Nombre": forms.TextInput(attrs={ 
                "class":"form-control", "placeholder":"Ingrese el nombre del crítico"
            },),
            "Email": forms.EmailInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el email"
            })
        }


class FormularioReseña(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = "__all__"
        labels = { 
            'texto': 'Reseña',
            'libro': 'Libro',
            'critico': 'Crítico',
        }
        widgets = {
            "texto": forms.Textarea(attrs={ 
                "class": "form-control", 
                "placeholder": "Ingrese el texto de la reseña",
                "rows": 5,
            }),
            "libro": forms.Select(attrs={ 
                "class": "form-control",
            }),
            "critico": forms.Select(attrs={ 
                "class": "form-control",
            }),
        }
    libro = forms.ModelChoiceField(
        queryset=Libro.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Seleccione un libro"
    )
    critico = forms.ModelChoiceField(
        queryset=Critico.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Seleccione un crítico"
    )