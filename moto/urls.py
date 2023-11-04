from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path("motos/listar", views.lista_motos, name="lista_moto"),
    path("motos/anyo", views.motos_desc, name="motos_desc"),
    path("motos/evento/<str:texto>", views.eventos_reservados, name="reserva_evento"),
    path("motos/eventofecha", views.evento_ascendente, name="reserv_asc"),
    path("motos/ultima_reserva", views.ult_reserva , name="ult_cliente"),
    path("motos/talla", views.talla_boutique, name="talla_m")
]

