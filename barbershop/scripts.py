from .models import *
from datetime import date, time

def crear_datos_prueba():
    # Crear usuarios
    admin = Usuario.objects.create(cedula=1, nombre="Admin", apellido="General", password="admin123", rol="A")
    barbero1 = Usuario.objects.create(cedula=2, nombre="Finn", apellido="Barbero", password="barbero123", rol="B")
    barbero2 = Usuario.objects.create(cedula=3, nombre="Jake", apellido="Barbero", password="barbero456", rol="B")
    cliente1 = Usuario.objects.create(cedula=4, nombre="Fuego", apellido="Cliente", password="cliente123", rol="U")
    cliente2 = Usuario.objects.create(cedula=5, nombre="Dulce", apellido="Cliente", password="cliente456", rol="U")

    # Crear servicios
    corte = Servicios.objects.create(nombre_servicio="Corte de Cabello", precio=15000)
    barba = Servicios.objects.create(nombre_servicio="Afeitado", precio=10000)

    # Crear citas
    Cita.objects.create(usuario=cliente1, barbero=barbero1, servicio=corte, fecha=date(2025, 6, 1), hora=time(10, 0))
    Cita.objects.create(usuario=cliente2, barbero=barbero2, servicio=barba, fecha=date(2025, 6, 2), hora=time(14, 30))

    print("Datos de prueba creados exitosamente.")
