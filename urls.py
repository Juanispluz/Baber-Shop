from django.urls import path
from . import views

# Urls de la aplicación facturación

urlpatterns = [
    # Inicio
    path("", views.index, name="index"),
    path('modificar-cita/<int:cedula_usuario>/', views.modificar_cita, name='modificar_cita'),
    
]
