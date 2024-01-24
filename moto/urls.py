from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path("motos/listar", views.lista_motos, name="lista_moto"),
    path("motos/anyo/<int:idus>", views.motos_desc, name="motos_desc"),
    path("motos/eventos_lista", views.eventos_listar, name="lista_eventos"),
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
    #crud para motos
    path("formulario/moto", views.moto_create, name="formulario_moto"),
    path('motos/buscar',views.moto_buscar,name='moto_buscar'),
    path('moto/buscar_avanzado/',views.moto_buscar_avanzado,name='moto_buscar_avanzado'),
    path('formulario/motos_editar/<int:moto_id>',views.moto_editar,name='moto_editar'),
    #crud para concesionarios
    path("formulario/concesionario", views.concesionario_create, name="formulario_concesionario"),
    path("formulario/concesionario_busqueda", views.concesionario_busqueda_avanzada, name="concesionarios_buscar"),
    path('formulario/concesionario_editar/<int:concesionario_id>',views.concesionario_editar,name='concesionario_editar'),
    #CRUD PARA ARTICCULOS
    path("formulario/articulo", views.artículo_create, name="formulario_articulo"),
    path("formulario/articulo_busqueda", views.articulo_busqueda_avanzada, name="articulos_buscar"),
    path('formulario/articulo_editar/<int:articulo_id>',views.articulo_editar,name='articulo_editar'),
    #crud para eventos
    path("formulario/evento", views.evento_create, name="formulario_evento"),
    path("formulario/evento_busqueda", views.evento_busqueda_avanzada, name="eventos_buscar"),
    path('formulario/evento_editar/<int:evento_id>',views.evento_editar,name='formulario_editar'),
    #crud para usuarios
    path("formulario/usuario", views.usuario_create, name="formulario_usuario"),
    path("formulario/usuario_busqueda", views.usuario_busqueda_avanzada, name="usuarios_buscar"),
    path('formulario/usuario_editar/<int:usuario_id>',views.usuario_editar,name='usuario_editar'),
    #crud para trabajador
    path("formulario/trabajador", views.trabajador_create, name="formulario_trabajador"),
    path("formulario/trabajador_busqueda", views.trabajador_busqueda_avanzada, name="trabajador_buscar"),
    path('formulario/trabajador_editar/<int:trabajador_id>',views.trabajador_editar,name='trabajador_editar'),
    #CRUD EXAMEN
    path("formulario/promocion", views.promocion_create, name="formulario_promocion"),
    path("formulario/promocion_busqueda", views.promocion_busqueda_avanzada, name="promocion_buscar"),
    path('formulario/promocion_editar/<int:promocion_id>',views.promocion_editar,name='promocion_editar'),
    
    #login
    path('registrar',views.registrar_usuario,name='registrar_usuario'),
    
    

]

