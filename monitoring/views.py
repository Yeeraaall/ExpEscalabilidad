from django.shortcuts import render
from imgmris.logic.logic_imgmri import cargarPrueba

def index(request):
    cargarPrueba()
    return render(request, 'index.html')