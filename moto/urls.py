from django.urls import path, re_path
from .import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path("motos/listar", views.lista_motos, name="lista_moto"),
    path("motos/anyo", views.motos_desc, name="motos_desc")
]