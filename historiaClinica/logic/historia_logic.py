from ..models import HistoriaClinica

def get_historias():
    queryset = HistoriaClinica.objects.all()
    return (queryset)

def create_historia(form):
    measurement = form.save()
    measurement.save()
    return ()