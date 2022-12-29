from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse('hola_mundo')

def otra_mas(request):
    return HttpResponse('si otras mas')

def fecha_actual(request):
    hoy = datetime.now().date()
    return HttpResponse(f'la fecha de hoy es {hoy}')

def vista_con_edad(request,edad):
    return HttpResponse(f'¿esto funciona?la edad es {edad} años')

def vista_con_template(request):
    return render(request,'template.html', context={})