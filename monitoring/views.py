from django.shortcuts import render
from imgmris.logic.logic_imgmri import cargarPrueba
from django.http import HttpResponse

def index(request):
    cargarPrueba()
    return render(request, 'index.html')

def healtCheck(request):
    return HttpResponse('ok')