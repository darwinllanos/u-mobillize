from django import forms #Se importa una caracteristica de django llamada forms
from .models import Viaje

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))#Esto es para enviarselo al html, html me estaria mostrando algo similar a un input, el widget=forms.TextInput(attrs={'class': 'input'}) sirve para aplicar los estilos al formulario
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['origen', 'destino', 'conductor', 'hora_llegada']


        
