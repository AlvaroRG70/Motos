from django.urls import path
from .api_views import *

urlpatterns = [
    path('motos', moto_list),
    path('motos/<int:moto_id>', moto_obtener),
    path('conc', concesionario_list),
    path('eventos', evento_list),
    path('usuarios', usuario_list),
    path('motos/busqueda_simple', moto_buscar_api),
    path('motos/busqueda_avanzada', moto_buscar_avanzado_api),
    path('concesionario/busqueda_avanzada', concesionario_busqueda_avanzada_api),
    path('evento/busqueda_avanzada', evento_busqueda_avanzada_api),
    path('motos/crear',moto_create),
    path('motos/editar/<int:moto_id>',moto_editar),
    path('concesionario/crear',concesionario_create),
    
    
]
