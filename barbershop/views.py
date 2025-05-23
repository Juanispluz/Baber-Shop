from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    return render(request, 'contacto.html')

def home(request):
    return render(request, 'home.html')
