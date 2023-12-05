from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path("motos/listar", views.lista_motos, name="lista_moto"),
    path("motos/anyo/<int:idus>", views.motos_desc, name="motos_desc"),
    path("motos/eventos/<str:texto>", views.eventos_reservados, name="reserva_evento"),
    path("motos/eventofecha", views.evento_ascendente, name="reserv_asc"),
    path("motos/ultima_reserva", views.ult_reserva , name="ult_cliente"),
    path("motos/talla", views.talla_boutique, name="talla_m"),
    path("motos/anyomay", views.moto_anyos, name="moto_anyo"),
    path("motos/trabajadornulo", views.concesionario_sin, name="concesionario_sin"),
    path("motos/concesionario_lista", views.concesionario_lista, name="lista_concesionario"),
    path("motos/concesionario_nac/<int:anyo>", views.nacidos_2018, name="anyo_apertura"),
    path("motos/concesionatio_i/<int:anyo>/<str:letra>", views.menor_2000 , name="contieneanyo"),
    path("motos/media", views.operaciones, name="operacionesmedia"),
    path("motos/nombre", views.nombre_descripcion, name="nombre_desc"),
    path("motos/ultima-votacion/<int:id_moto>", views.ult_votacion, name="votacion_ultima"),
    path("motos/puntuacion/<int:id_usuario>", views.con_3_puntos, name="3_puntos"),
    path("motos/usuario-sin-voto", views.usuario_sin_voto, name="usuario_sin"),
    path("motos/bancos/<str:nombre>", views.cuentas_bancos, name="bancos_nombre"),
    path("motos/medias", views.modelos_con_media_mayor_2_5, name="modelos_moto"),
    path("motos/moto/<int:id_moto>", views.moto_unica, name="moto"),
    path("motos/evento/<int:id_evento>", views.evento_unico, name="evento"),
    path("motos/concesionario/<int:id_concesionario>", views.concesionario_unico, name="concesionario"),
    path("formulario/moto", views.moto_create, name="formulario_moto"),
    path("formulario/concesionario", views.concesionario_create, name="formulario_concesionario"),
    path('motos/buscar',views.moto_buscar,name='moto_buscar'),
    path('libro/buscar_avanzado/',views.moto_buscar_avanzado,name='moto_buscar_avanzado'),
]

