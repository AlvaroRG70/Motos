from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path("motos/listar", views.lista_motos, name="lista_moto"),
    path("motos/anyo/<int:idus>", views.motos_desc, name="motos_desc"),
    path("motos/evento/<str:texto>", views.eventos_reservados, name="reserva_evento"),
    path("motos/eventofecha", views.evento_ascendente, name="reserv_asc"),
    path("motos/ultima_reserva", views.ult_reserva , name="ult_cliente"),
    path("motos/talla", views.talla_boutique, name="talla_m"),
    path("motos/anyomay", views.moto_anyos, name="moto_anyo"),
    path("motos/trabajadornulo", views.concesionario_sin, name="concesionario_sin"),
    path("motos/concesionario_nac/<int:anyo>", views.nacidos_2018, name="anyo_apertura"),
    path("motos/concesionatio_i/<int:anyo>/<str:letra>", views.menor_2000 , name="contieneanyo"),
    path("motos/media", views.operaciones, name="operacionesmedia"),
    path("motos/nombre", views.nombre_descripcion, name="nombre_desc")
]

