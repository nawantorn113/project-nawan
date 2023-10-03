from django.shortcuts import render
from . import models

# Create your views here.


def Index(request):
    context = {}
    i = models.Employee.objects.all().order_by("name")

    context["employees"] = i
    return render(request, "index.html", context)


def Department(request, id):
    context = {}
    i = models.Employee.objects.filter(department=id)
    context["departments"] = i
    
    return render(request, "department.html", context,)

def About(request):
    return render(request, "about.html",)