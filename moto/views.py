from django.shortcuts import render
from moto.models import Moto, Evento, ReservaEvento, Boutique
from django.db.models import Q,Prefetch

# Create your views here.
def index(request):
    return render(request, 'index.html')

#Una url que muestre todas sus motos y los datos

def lista_motos(request):
    motos = (Moto.objects.prefetch_related("usuario")).all()
    return render(request, "motos/lista.html", {"lista_moto":motos})

#Una url que muestre todas las motos que están asociadas a un usuario, ordenadas por año descendente.

def motos_desc(request):
    motos = (Moto.objects.prefetch_related("usuario", Prefetch("VentaMoto"))).all()
    motos = motos.order_by("-año")
    return render(request, "motos/desc.html", {"motos_desc":motos})

#Crear una URL que muestre todas los eventos que tengan un texto en concreto en la descripción a la hora de asignarlas a una reserva (usuario).

def eventos_reservados(request,texto):
    eventos = (Evento.objects.prefetch_related("usuario")).all()
    eventos = eventos.filter(descripcion__contains = texto)
    return render(request, "evento/evento.html", {"reserva_evento":eventos})

#crear una URl que muestre los usuarios asigados a una reserva de evento ordenados por fecha de evento de forma ascendente
#no se mostrar la fecha de reserva

def evento_ascendente(request):
    evento = (Evento.objects.prefetch_related("usuario").order_by("reservaevento__fecha_reserva")).all()
    return render(request, "evento/reserva.html", {"reserv_asc":evento, "fecha":reserva})

#Crea una URL que muestre la compra más reciente realizada por un usuario, incluyendo el nombre del producto, la cantidad, el precio y la fecha de compra.

# Crear una URL que obtenga el último usuario que ha reservado un evento.

def ult_reserva(request):
    cliente = Evento.objects.prefetch_related("usuario").all()
    cliente = cliente.order_by("-reservaevento__fecha_reserva")[:1].get()
    return render(request, "evento/ult_cliente.html", {"ult_cliente":cliente})

#muestra el nombre de los elementos de la boutique cuya talla sea Medium

def talla_boutique(request):
    tallas = (Boutique.objects.filter(talla = "MM")).all()
    return render(request, "boutique/tallam.html", {"talla_m":tallas})

"""
Lista de Usuarios:
Crea una URL que muestre una lista de todos los usuarios registrados en la aplicación con sus nombres y apellidos.

Tareas de un Trabajador:
Crea una URL que muestre todas las motos asociadas a un trabajador específico, ordenadas por la marca y el modelo.

Accesorios de una Moto:
Crea una URL que muestre todos los accesorios disponibles para una moto en particular, incluyendo su nombre, marca y precio.

Boutique de Concesionario:
Crea una URL que muestre todos los productos disponibles en la boutique de un concesionario en particular, con detalles como nombre, tipo, descripción, talla y precio.

Eventos de un Usuario:
Crea una URL que muestre todos los eventos a los que un usuario ha reservado asistencia, incluyendo detalles como nombre del evento, fecha y hora.

Compras más Recientes de un Usuario:
Crea una URL que muestre la compra más reciente realizada por un usuario, incluyendo el nombre del producto, la cantidad, el precio y la fecha de compra.

Ventas de una Moto:
Crea una URL que muestre todas las ventas relacionadas con una moto en particular, incluyendo detalles de la compra y el usuario.

Ventas de un Concesionario:
Crea una URL que muestre todas las ventas realizadas por un concesionario en particular, incluyendo detalles de la compra y la moto.

Reservas de un Evento:
Crea una URL que muestre todas las reservas de un evento específico, incluyendo detalles de la reserva y el usuario.
"""