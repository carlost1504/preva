from django import forms
from django.contrib.auth.models import User

class form_Donacion(forms.Form):
    Cantidad = forms.IntegerField(label='Cantidad')
    Fecha = forms.DateField(label='Fecha')
    Codigo = forms.CharField(label='Código', max_length=50)
    Remitente = forms.CharField(label='Remitente', max_length=50)
    Destinatario = forms.CharField(label='Destinatario', max_length=50)
    PATROCINADORCedula = forms.CharField(label='Cédula de patrocinador', max_length=15)

class MyForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=255)
    codigo = forms.CharField(label='Código', max_length=255)

