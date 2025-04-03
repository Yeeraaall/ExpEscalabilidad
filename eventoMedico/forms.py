from django import forms
from .models import EventoMedico

class ImgMriForm(forms.ModelForm):
    class Meta:
        model = EventoMedico
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
