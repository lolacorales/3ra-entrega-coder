from django import forms

class NuevoLibro(forms.Form):
    titulo = forms.CharField(max_length=100)
    año = forms.IntegerField()
    autor = forms.CharField(max_length=100)