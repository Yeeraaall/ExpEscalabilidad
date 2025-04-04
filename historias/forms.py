from django import forms
from .models import Historia

class HistoriaForm(forms.ModelForm):
    class Meta:
        model = Historia
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