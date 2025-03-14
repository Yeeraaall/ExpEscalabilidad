from django.db import models


class Examen(models.Model):
    solicitud = models.IntegerField(primary_key=True)
    paciente = models.CharField(max_length=100)
    cc=models.IntegerField()
    fecha = models.DateField()
    
    def __str__(self):
        return '%s' % (self.solicitud)
