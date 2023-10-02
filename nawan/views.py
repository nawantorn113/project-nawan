from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    context = {}
    context['nawan'] = models. history.objects.all()
    return render(request, 'index.html', context)


def (request, id):
    context = {}
    context['nawan'] = models. history.objects.filter(personal information=name)

    return render(request, ' history.html', context)