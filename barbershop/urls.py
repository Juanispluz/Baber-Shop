from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("quienes-somos/", views.quienes_somos, name="quienes_somos"),
    path("servicios/", views.servicios, name="servicios"),
    path("contacto/", views.contacto, name="contacto"),
    
    # Citas
    path('eliminar-cita/<int:cita_id>/', views.eliminar_cita, name='eliminar_cita'),
    path('formulario-editar-cita/<int:cedula_usuario>/', views.formulario_editar_cita, name='formulario_editar_cita'),
    path('reservar/', views.reservar_cita, name='reservar_cita'),
    path('reserva-exitosa/', views.reserva_exitosa, name='reserva_exitosa'),
    path('buscar-citas/', views.buscar_citas, name='buscar_citas'),
    
    # Servicios de spa/relajación
    path('services/', views.index, name='services'),
    path('service-list/', views.service_list, name='service_list'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
]