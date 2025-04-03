from django import forms
from .models import HistoriaClinica

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = [
            'id',
            'paciente',
            'cc',
            #'fecha',
        ]
        labels = {
            'id' : 'Id',
            'paciente' : 'Paciente',
            'cc' : 'CC',
            #'fecha' : 'Fecha',
        }