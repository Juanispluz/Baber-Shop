from django.contrib import admin
from .models import *

# Register your models here.

class Usuario_Admin(admin.ModelAdmin):
    list_display = ["cedula", "nombre", "apellido", 'rol']

class Servicios_Admin(admin.ModelAdmin):
    list_display = ["id", "nombre_servicio"]

class Cita_Admin(admin.ModelAdmin):
    list_display = ["id", "usuario", "barbero", "fecha", "hora", "estado"]

admin.site.register(Usuario, Usuario_Admin)
admin.site.register(Servicios, Servicios_Admin)
admin.site.register(Cita, Cita_Admin)
