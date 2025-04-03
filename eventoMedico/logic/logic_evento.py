from ..models import EventoMedico

def get_eventos():
    queryset = EventoMedico.objects.all()
    return (queryset)

def create_evento(form):
    measurement = form.save()
    measurement.save()
    return ()


