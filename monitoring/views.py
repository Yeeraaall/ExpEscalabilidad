from django.shortcuts import render
from django.http import HttpResponse
from historia.models import Historia

def index(request):
    a=Historia.objects.all()
    if len(a) == 0:
        Historia.objects.create(id=1, paciente='Juan', cc=123456)
    return render(request, 'index.html')

def healthCheck(request):
    return HttpResponse('ok')