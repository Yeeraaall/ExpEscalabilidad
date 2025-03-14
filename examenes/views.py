from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ExamenForm
from .logic.examen_logic import get_examenes, create_examen

def variable_list(request):
    examenes = get_examenes()
    context = {
        'examen_list': examenes
    }
    return render(request, 'Examen/examenes.html', context)

def examen_create(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            create_examen(form)
            messages.add_message(request, messages.SUCCESS, 'Examen creado')
            return HttpResponseRedirect(reverse('examenCreate'))
        else:
            print(form.errors)
    else:
        form = ExamenForm()

    context = {
        'form': form,
    }
    return render(request, 'Examen/examenCreate.html', context)