from django.shortcuts import render
from moto.models import Moto, Evento, ReservaEvento, Boutique, Concesionario
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
    motos = (Moto.objects.prefetch_related("usuario")).all()
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
    return render(request, "evento/reserva.html", {"reserv_asc":evento, "fecha":evento})


# Crear una URL que obtenga el último usuario que ha reservado un evento.
'''
def ult_reserva(request):
    cliente = Evento.objects.prefetch_related("usuario").all()
    cliente = cliente.order_by("-reservaevento__fecha_reserva")[:1].get()
    return render(request, "evento/ult_cliente.html", {"ult_cliente":cliente})
'''

def ult_reserva(request):
    cliente = ReservaEvento.objects.select_related("usuario", "evento").all()
    cliente = cliente.order_by("-fecha_reserva")[:1].get()
    return render(request, "evento/ult_cliente.html", {"ult_cliente":cliente})

#muestra el nombre de los elementos de la boutique cuya talla sea Medium

def talla_boutique(request):
    tallas = (Boutique.objects.filter(talla = "MM")).all()
    return render(request, "boutique/tallam.html", {"talla_m":tallas})

#muentra las motos con sus usuarios asociados con año de moto mayor a 10000

def moto_anyos(request):
    moto = (Moto.objects.prefetch_related("usuario")).all()
    moto = moto.filter(año__gt = 10000)
    return render(request, "motos/motoanyo.html", {"moto_anyo":moto})

#muestra los concesionarios que no tienen un trabajador asociado


def concesionario_sin(request):
    concesionario = (Concesionario.objects.prefetch_related(Prefetch("trabajador_concesionario"))).all()
    concesionario = concesionario.filter(trabajador_concesionario__nombre = None)
    return render(request, "concesionario/sin.html", {"concesionario_sin":concesionario})

#muestra los concesionarios que abrieron en 1983 con sus trabajadores

def nacidos_2018(request, anyo):
    concesionario = (Concesionario.objects.prefetch_related(Prefetch("trabajador_concesionario")).filter(fecha_apertura__year=anyo)).all()
    return render(request, "concesionario/anyo_apert.html", {"anyo_apertura":concesionario})

#muestra los concesionarios cuya fecha de apertura sea menor a 2000 y contengan en su descripcion la letra i

def menor_2000(request, anyo, letra):
    concesionario = (Concesionario.objects.filter(fecha_apertura__year__lt=anyo).filter(descripcion__contains = letra)).all()
    return render(request, "concesionario/contieneanyo.html", {"contieneanyo":concesionario})


def mi_error_404(request, exception=None):
    return render(request, "errores/404.html",None,None,404)

def mi_error_400(request, exception=None):
    return render(request, "errores/400.html",None,None,400)

def mi_error_403(request, exception=None):
    return render(request, "errores/403.html",None,None,403)

def mi_error_500(request, exception=None):
    return render(request, "errores/500.html",None,None,500)