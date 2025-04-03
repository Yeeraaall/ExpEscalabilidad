from django.db import models
from historiaClinica.models import HistoriaClinica


class EventoMedico(models.Model):
    fecha=models.DateField()
    historiaPaciente=models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE, default=None)
    especialidad=models.CharField(max_length=100, default="Consulta General")
    comentarios=models.TextField(default=None)
    
    def __str__(self):
        return '{}'.format(self.historiaPaciente.id+' - '+self.fecha.strftime('%Y-%m-%d')+' - '+self.especialidad[0:4])