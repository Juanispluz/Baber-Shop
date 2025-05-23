from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quienes-somos/", views.quienes_somos, name="quienes_somos"),
    path("servicios/", views.servicios, name="servicios"),
    path("contacto/", views.contacto, name="contacto"),
    
    # Citas
    path("cancelar-cita/<int:cita_id>/", views.cancelar_cita, name="cancelar_cita"),
    path('modificar-cita/<int:cedula_usuario>/', views.modificar_cita, name='modificar_cita'),
    path('reservar/', views.reservar_cita, name='reservar_cita'),
    path('reserva-exitosa/', views.reserva_exitosa, name='reserva_exitosa'),
    
    # Servicios de spa/relajación
    path('services/', views.index, name='services'),
    path('service-list/', views.service_list, name='service_list'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
]