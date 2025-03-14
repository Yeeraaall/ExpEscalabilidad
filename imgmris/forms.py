from django import forms
from .models import ImgMri

class ImgMriForm(forms.ModelForm):
    class Meta:
        model = ImgMri
        fields = [
            'examen',
            'url'
        ]

        labels = {
            'examen' : 'Examen',
            'url' : 'Url'
        }
