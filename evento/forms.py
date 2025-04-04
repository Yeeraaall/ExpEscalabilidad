from django import forms
from .models import Evento

class ImgMriForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'fecha',
            'historiaPaciente',
            'especialidad',
            'comentarios'
            
        ]

        labels = {
            'fecha':'Fecha',
            'historiaPaciente':'Historia Clinica',
            'especialidad':'Especialidad',
            'comentarios':'Comentarios'
        }
