from django.shortcuts import render
from django.http import HttpResponse
from ..historiaClinica.models import HistoriaClinica

def index(request):
    a=HistoriaClinica.objects.all()
    if len(a) == 0:
        HistoriaClinica.objects.create(id=1, paciente='Juan', cc=123456)
    return render(request, 'index.html')

def healthCheck(request):
    return HttpResponse('ok')