from django.db import models
from examenes.models import Examen


class ImgMri(models.Model):
    url=models.CharField(max_length=500)
    examen=models.ForeignKey(Examen, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return '{}'.format(self.url)