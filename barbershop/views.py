from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Cita

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

def cancelar_cita(request, cita_id):
    if request.method == 'POST':
        cita = get_object_or_404(Cita, id=cita_id)

        if request.user != cita.usuario:
            return JsonResponse({'error': 'No tienes permiso para cancelar esta cita.'}, status=403)

        exito, mensaje = cita.cancelar()
        if not exito:
            return JsonResponse({'error': mensaje}, status=400)

        return JsonResponse({'mensaje': mensaje})
    
    return JsonResponse({'error': 'Método no permitido.'}, status=405)