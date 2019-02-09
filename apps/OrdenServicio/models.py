from django.db import models
from django.contrib.auth.models import User

class OrdenServicio(models.Model):
    servicio_vendido = models.CharField(max_length=100) # ¿string o Modelo Servicio?
    valor_servicio = models.PositiveIntegerField() # ¿string o Modelo Servicio?
    encargado = models.CharField(max_length=100) # Datos Maestros?
    cliente = models.CharField(max_length=100) # Datos Maestros?
    comentarios = models.CharField(max_length=300)

    # Constantes para OrdenServicio
    ASIGNADA = 'AS'
    TRAMITE = 'TR'
    CANCELADA = 'CA'
    CERRADA = 'CE'
    # Fin Constantes

    opciones_estado = (
        (ASIGNADA, 'Asignada'),
        (TRAMITE, 'Tramite'),
        (CANCELADA, 'Cancelada'),
        (CERRADA, 'Cerrada'),
    )
    estado = models.CharField(
        max_length=1,
        choices=opciones_estado,
        default=ASIGNADA,
    )
