from django.urls import path
from . import views

# Urls de la aplicación facturación

urlpatterns = [
    # Inicio
    path("", views.index, name="index"),
    path('services/', views.index, name='services'),
    path('service-list/', views.service_list, name='service_list'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
]