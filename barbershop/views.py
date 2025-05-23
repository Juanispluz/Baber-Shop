from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def servicios(request):
    servicios_list = Servicios.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios_list})

def contacto(request):
    return render(request, 'contacto.html')

def cancelar_cita(request, cita_id):
    if request.method == 'POST':
        cita = get_object_or_404(Cita, id=cita_id)
        
        if request.user != cita.usuario:
            return JsonResponse({'error': 'No tienes permiso para cancelar esta cita.'}, status=403)

        cita.estado = 'C'
        cita.save()
        return JsonResponse({'mensaje': 'Cita cancelada correctamente'})
    
    return JsonResponse({'error': 'Método no permitido.'}, status=405)

@require_http_methods(["PUT"])
def modificar_cita(request, cedula_usuario):
    try:
        data = json.loads(request.body)
        usuario = get_object_or_404(Usuario, cedula=cedula_usuario)
        cita = get_object_or_404(Cita, usuario=usuario, estado='P')

        # Actualizar fecha si se proporciona
        if 'fecha' in data:
            try:
                cita.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Formato de fecha inválido'}, status=400)

        # Actualizar hora si se proporciona
        if 'hora' in data:
            try:
                cita.hora = datetime.strptime(data['hora'], '%H:%M').time()
            except ValueError:
                return JsonResponse({'error': 'Formato de hora inválido'}, status=400)

        # Actualizar barbero si se proporciona
        if 'barbero_id' in data:
            nuevo_barbero = get_object_or_404(Usuario, cedula=data['barbero_id'], rol='B')
            # Verificar disponibilidad del barbero
            if Cita.objects.filter(barbero=nuevo_barbero, fecha=cita.fecha, hora=cita.hora).exclude(id=cita.id).exists():
                return JsonResponse({'error': 'El barbero no está disponible'}, status=400)
            cita.barbero = nuevo_barbero

        cita.save()
        return JsonResponse({'mensaje': 'Cita modificada correctamente'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def reservar_cita(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            usuario_id = request.POST.get('usuario')
            barbero_id = request.POST.get('barbero')
            servicio_id = request.POST.get('servicio')
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')

            # Validar y crear la cita
            usuario = get_object_or_404(Usuario, cedula=usuario_id)
            barbero = get_object_or_404(Usuario, cedula=barbero_id, rol='B')
            servicio = get_object_or_404(Servicios, id=servicio_id)

            # Verificar disponibilidad
            if Cita.objects.filter(barbero=barbero, fecha=fecha, hora=hora).exists():
                messages.error(request, 'El barbero no está disponible en ese horario')
                return render(request, 'reserva_form.html', {
                    'barberos': Usuario.objects.filter(rol='B'),
                    'servicios': Servicios.objects.all(),
                    'usuarios': Usuario.objects.filter(rol='U')  # Asegúrate de pasar los usuarios
                })

            # Crear la cita
            Cita.objects.create(
                usuario=usuario,
                barbero=barbero,
                servicio=servicio,
                fecha=fecha,
                hora=hora,
                estado='P'
            )

            messages.success(request, 'Cita reservada con éxito')
            return redirect('reserva_exitosa')

        except Exception as e:
            messages.error(request, f'Error al reservar cita: {str(e)}')
            return render(request, 'reserva_form.html', {
                'barberos': Usuario.objects.filter(rol='B'),
                'servicios': Servicios.objects.all(),
                'usuarios': Usuario.objects.filter(rol='U')
            })

    # Si es GET, mostrar formulario con datos necesarios
    return render(request, 'reserva_form.html', {
        'barberos': Usuario.objects.filter(rol='B'),
        'servicios': Servicios.objects.all(),
        'usuarios': Usuario.objects.filter(rol='U')
    })

def reserva_exitosa(request):
    return render(request, 'reserva_exitosa.html')

# Lógica para los servicios de spa/relajación
def service_list(request):
    service_type = request.GET.get('type', '').lower()
    services_data = {
        'massages': [
            {'id': 1, 'name': 'Deep Swedish Massage', 'image': '/static/images/sweedish.jpg', 'price': '$410', 'hours': '2 Hours & 20 Min'},
            {'id': 2, 'name': 'Reflexology Massage', 'image': '/static/images/patas.jpg', 'price': '$550', 'hours': '2 Hours & 15 Min'},
            {'id': 3, 'name': 'Modelage Massage', 'image': '/static/images/modelage.jpg', 'price': '$280', 'hours': '90 Min'},
        ],
        'facials': [
            {'id': 4, 'name': 'Seaweed Infusion', 'image': '/static/images/infusion.jpg', 'price': '$145', 'hours': '30 min'},
            {'id': 5, 'name': 'Microdermabrasion Crystal', 'image': '/static/images/micro.jpg', 'price': '190', 'hours': '45 min'},
            {'id': 6, 'name': 'Black Facial', 'image': '/static/images/black.jpg', 'price': '$145', 'hours': '30 min'},
        ],
        'packages': [
            {'id': 7, 'name': 'Amazonian Ritual', 'image': '/static/images/amazonia.jpg', 'price': '$120', 'hours': '2 Hours & 30 Min'},
            {'id': 8, 'name': 'Japanese Celebration', 'image': '/static/images/jap.jpg', 'price': '$100', 'hours': '2 Hours'},
            {'id': 9, 'name': 'Cozy Ritual', 'image': '/static/images/cozy.jpg', 'price': '$150', 'hours': '2 Hours & 30 Min'},
        ],
    }
    
    services = services_data.get(service_type, [])
    return render(request, 'service_list.html', {
        'services': services,
        'service_type': service_type.capitalize()
    })

def service_detail(request, service_id):
    all_services = []
    services_data = {
        'massages': [
            {'id': 1, 'name': 'Deep Swedish Massage', 'image': '/static/images/sweedish.jpg', 'price': '$410', 'hours': '2 Hours & 20 Min'},
            {'id': 2, 'name': 'Reflexology Massage', 'image': '/static/images/patas.jpg', 'price': '$550', 'hours': '2 Hours & 15 Min'},
            {'id': 3, 'name': 'Modelage Massage', 'image': '/static/images/modelage.jpg', 'price': '$280', 'hours': '90 Min'},
        ],
        'facials': [
            {'id': 4, 'name': 'Seaweed Infusion', 'image': '/static/images/infusion.jpg', 'price': '$145', 'hours': '30 min'},
            {'id': 5, 'name': 'Microdermabrasion Crystal', 'image': '/static/images/micro.jpg', 'price': '190', 'hours': '45 min'},
            {'id': 6, 'name': 'Black Facial', 'image': '/static/images/black.jpg', 'price': '$145', 'hours': '30 min'},
        ],
        'packages': [
            {'id': 7, 'name': 'Amazonian Ritual', 'image': '/static/images/amazonia.jpg', 'price': '$120', 'hours': '2 Hours & 30 Min'},
            {'id': 8, 'name': 'Japanese Celebration', 'image': '/static/images/jap.jpg', 'price': '$100', 'hours': '2 Hours'},
            {'id': 9, 'name': 'Cozy Ritual', 'image': '/static/images/cozy.jpg', 'price': '$150', 'hours': '2 Hours & 30 Min'},
        ],
    }
    
    for group in services_data.values():
        all_services.extend(group)
    
    service = next((s for s in all_services if s['id'] == int(service_id)), None)
    return render(request, 'service_detail.html', {'service': service})