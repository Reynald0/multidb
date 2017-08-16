from django.http import HttpResponse
from django.shortcuts import render

def insertar(request):
    from mi_app_2.models import MiApp2Model
    MiApp2Model.objects.create(nombre="Reynald0").save()
    return HttpResponse("Insertado")
