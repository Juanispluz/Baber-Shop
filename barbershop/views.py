from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CitaForm

def index(request):
    return render(request, 'index.html')

def reservar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita reservada con éxito.')
            return redirect('reserva_exitosa')
    else:
        form = CitaForm()
    return render(request, 'reserva_form.html', {'form': form})

def reserva_exitosa(request):
    return render(request, 'reserva_exitosa.html')


# Logica para los Details de los Services

def service_list(request):
    service_type = request.GET.get('type')
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
    return render(request, 'service_list.html', {'services': services, 'service_type': service_type})

def service_detail(request, service_id):
    # Flatten all services into a single list
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
