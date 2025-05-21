from django.db import models # type: ignore

# Create your models here.
class Usuario(models.Model):
    cedula = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=254)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ROLES = (
        ('A', 'Administrador'),
        ('B', 'Barbero'),
        ('U', 'Usuario')
    )
    rol = models.CharField(max_length=1, choices=ROLES, default='U')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Servicios(models.Model):
    id = models.AutoField(primary_key=True,)
    nombre_servicio = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_servicio} - {self.precio}"


class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='citas_usuario')
    barbero = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='citas_barbero', limit_choices_to={'rol': 'B'})
    servicio = models.ForeignKey(Servicios, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    ESTADOS = (
        ('P', 'Pendiente'),
        ('C', 'Cancelada'),
        ('R', 'Realizada')
    )
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')

    def __str__(self):
        return f"{self.usuario} - {self.fecha} {self.hora}"

    def cancelar(self):
        if self.estado != 'P':
            return False, "Solo se pueden cancelar citas pendientes."
        
        self.estado = 'C'
        self.save()
        return True, "Cita cancelada exitosamente."