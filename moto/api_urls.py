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
    path('motos/editar/nombre/<int:moto_id>',moto_actualizar_nombre),
    path('motos/eliminar/<int:moto_id>',moto_eliminar),
    
    path('concesionario/<int:concesionario_id>', concesionario_obtener),
    path('concesionario/crear',concesionario_create),
    path('concesionario/editar/<int:concesionario_id>',concesionario_editar),
    path('concesionario/editar/nombre/<int:concesionario_id>',concesionario_actualizar_nombre),
    path('concesionario/eliminar/<int:concesionario_id>',concesionario_eliminar),
    
    path('evento/<int:evento_id>', evento_obtener),
    path('evento/crear',evento_create),
    path('evento/editar/<int:evento_id>',evento_editar),
    path('evento/eliminar/<int:evento_id>',evento_eliminar),
    
    
]
