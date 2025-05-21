from django.urls import path
from . import views

# Urls de la aplicación facturación
urlpatterns = [
    path("", views.index, name="index"),
    path("cancelar-cita/<int:cita_id>/", views.cancelar_cita, name="cancelar_cita"),
]