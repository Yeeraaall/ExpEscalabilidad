from django import forms
from .models import Examen

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = [
            'solicitud',
            'paciente',
            'cc',
            #'fecha',
        ]
        labels = {
            'solicitud' : 'Solicitud',
            'paciente' : 'Paciente',
            'cc' : 'CC',
            #'fecha' : 'Fecha',
        }