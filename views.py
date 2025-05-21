from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Cita, Usuario
from django.views.decorators.http import require_http_methods
from django.db.models import Q
import json
from datetime import datetime

@require_http_methods(["PUT"])
def modificar_cita(request, cedula_usuario):
    data = json.loads(request.body)

    # Buscar usuario
    usuario = get_object_or_404(Usuario, cedula=cedula_usuario)

    # Buscar la cita activa (pendiente) del usuario
    cita = get_object_or_404(Cita, usuario=usuario, estado='P')

    # Modificacion de la fecha si viene en la petición
    nueva_fecha = data.get('fecha')
    nueva_hora = data.get('hora')
    if nueva_fecha:
        try:
            cita.fecha = datetime.strptime(nueva_fecha, '%Y-%m-%d').date()
        except ValueError:
            return JsonResponse({'error': 'Formato de fecha inválido. Usa YYYY-MM-DD'}, status=400)
    if nueva_hora:
        try:
            cita.hora = datetime.strptime(nueva_hora, '%H:%M').time()
        except ValueError:
            return JsonResponse({'error': 'Formato de hora inválido. Usa HH:MM'}, status=400)

    # Modificacion del barbero si se indica y está disponible en esa fecha y hora
    nuevo_barbero_id = data.get('barbero_id')
    if nuevo_barbero_id:
        nuevo_barbero = get_object_or_404(Usuario, cedula=nuevo_barbero_id, rol='B')
        # Verificacion de la disponibilidad del barbero uhhhh
        conflicto = Cita.objects.filter(
            barbero=nuevo_barbero,
            fecha=cita.fecha,
            hora=cita.hora
        ).exclude(id=cita.id).exists()
        if conflicto:
            return JsonResponse({'error': 'El barbero no está disponible en esa fecha y hora'}, status=400)
        cita.barbero = nuevo_barbero

    cita.save()
    return JsonResponse({'mensaje': 'Cita modificada correctamente'})
