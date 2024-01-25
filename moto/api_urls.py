from django.urls import path
from .api_views import *

urlpatterns = [
    path('motos', moto_list),
    path('conc', concesionario_list),
    path('eventos', evento_list),
    path('motos/busqueda_simple', moto_buscar_api),
    path('motos/busqueda_avanzada', moto_buscar_avanzado_api),
]