from ..models import Examen

def get_examenes():
    queryset = Examen.objects.all()
    return (queryset)

def create_examen(form):
    measurement = form.save()
    measurement.save()
    return ()