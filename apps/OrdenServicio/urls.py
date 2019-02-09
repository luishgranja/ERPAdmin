from django.urls import path
from apps.OrdenServicio.views import *

app_name = 'OrdenServicio'

urlpatterns = [
    path('crear-orden-servicio', crear_orden_servicio, name='crear_orden_servicio'),
]