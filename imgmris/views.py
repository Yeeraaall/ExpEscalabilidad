from django.shortcuts import render
from .forms import ImgMriForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_imgmri import create_imgmris, get_imgmris

def imgmri_list(request):
    imgs = get_imgmris()
    context = {
        'imgmri_list': imgs
    }
    return render(request, 'ImgMri/imgmris.html', context)

def imgmri_create(request):
    if request.method == 'POST':
        form = ImgMriForm(request.POST)
        if form.is_valid():
            create_imgmris(form)
            messages.add_message(request, messages.SUCCESS, 'Imagen cargada')
            return HttpResponseRedirect(reverse('imgmriCreate'))
        else:
            print(form.errors)
    else:
        form = ImgMriForm()

    context = {
        'form': form,
    }

    return render(request, 'ImgMri/imgmriCreate.html', context)