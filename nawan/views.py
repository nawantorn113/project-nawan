from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    context = {}
    context['nawans'] = models. history.objects.all()
    return render(request, 'index.html', context)


def history(request, id):
    context = {}
    context['nawans'] = models. history.objects.filter(personal_information=id)

    return render(request, ' history.html', context)