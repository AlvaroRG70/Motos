from django.shortcuts import render, redirect
from moto.models import Moto, Evento, ReservaEvento, Boutique, Concesionario, ValoracionMoto, Usuario, CuentaBancaria
from django.db.models import Q,Prefetch, Avg,Max,Min, F
from moto.forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def moto_unica(request,id_moto):
    motos = (Moto.objects.prefetch_related("usuario"))
    motos = motos.filter(id = id_moto).first()
    return render(request, "motos/mostrar_moto.html", {"moto":motos})

def evento_unico(request, id_evento):
    eventos = Evento.objects.prefetch_related("usuario")
    eventos =  eventos.filter(id = id_evento).first()
    return render(request, "evento/mostrar_evento.html", {"evento":eventos})

def concesionario_unico(request, id_concesionario):
    concesionarios = (Concesionario.objects.prefetch_related(Prefetch("trabajador_concesionario"))).all()
    concesionarios = concesionarios.filter(id = id_concesionario).first()
    return render(request, "concesionario/mostrar_concesionario.html", {"concesionario":concesionarios})

def concesionario_lista(request):
    concesionarios = (Concesionario.objects.prefetch_related("moto")).all()
    return render(request, "concesionario/lista_concesionario.html", {"concesionario_lista":concesionarios})

#Una url que muestre todas sus motos y los datos

def lista_motos(request):
    motos = (Moto.objects.prefetch_related("usuario")).all()
    return render(request, "motos/lista.html", {"lista_moto":motos})

#Una url que muestre todas las motos que están asociadas a un usuario, ordenadas por año descendente.

def motos_desc(request, idus):
    motos = (Moto.objects.prefetch_related("usuario")).all()
    motos = motos.filter(usuario__id = idus).order_by("-año")
    return render(request, "motos/desc.html", {"motos_desc":motos})

#Crear una URL que muestre todas los eventos que tengan un texto en concreto en la descripción a la hora de asignarlas a una reserva (usuario).

def eventos_reservados(request,texto):
    eventos = (Evento.objects.prefetch_related("usuario")).all()
    eventos = eventos.filter(descripcion__contains = texto)
    return render(request, "evento/evento.html", {"reserva_evento":eventos})

#crear una URl que muestre los usuarios asigados a una reserva de evento ordenados por fecha de evento de forma ascendente
#no se mostrar la fecha de reserva

def evento_ascendente(request):
    evento = (ReservaEvento.objects.select_related("usuario", "evento").order_by("fecha_reserva")).all()
    return render(request, "evento/reserva.html", {"reserv_asc":evento})


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


#haz la media, el max y el minimo del precio de todas las motos

def operaciones(request):
    resultado = Moto.objects.aggregate(Avg("precio"),Max("precio"),Min("precio"))
    media = resultado["precio__avg"]
    maximo = resultado["precio__max"]
    minimo = resultado["precio__min"]
    return render(request, "motos/operaciones.html", {"media":media, "maximo":maximo, "minimo":minimo})

#url que muestre los eventos que contienen su nombre en la descripcion

def nombre_descripcion(request):
    eventos = (Evento.objects.prefetch_related("usuario")).all()
    eventos = eventos.filter(descripcion__contains = F("nombre"))
    return render(request, "evento/contiene.html", {"nombre_desc":eventos})



def mi_error_404(request, exception=None):
    return render(request, "errores/404.html",None,None,404)

def mi_error_400(request, exception=None):
    return render(request, "errores/400.html",None,None,400)

def mi_error_403(request, exception=None):
    return render(request, "errores/403.html",None,None,403)

def mi_error_500(request, exception=None):
    return render(request, "errores/500.html",None,None,500)


#El último voto que se realizó en un modelo principal en concreto, y mostrar el comentario, la votación e información del usuario o cliente que lo realizó.

def ult_votacion(request, id_moto):
    votacion = (ValoracionMoto.objects.select_related("usuario", "moto")).all()
    votacion = votacion.filter(moto__id = id_moto).order_by("fecha_votacion")[:1].get()
    return render(request, "examen/ult_votacion.html", {"votacion_ultima":votacion})


#Todos los modelos principales que tengan votos con una puntuación numérica igual a 3 y que realizó un usuario o cliente en concreto. 

def con_3_puntos(request, id_usuario):
    puntos = (ValoracionMoto.objects.select_related("usuario", "moto"))
    puntos = puntos.filter(usuario__id = id_usuario).filter(puntuacion = 3)
    return render(request, "examen/3_puntos.html", {"3_puntos":puntos})


#Todos los usuarios o clientes que no han votado nunca y mostrar información sobre estos usuarios y clientes al completo..

def usuario_sin_voto(request):
    puntos = Usuario.objects.filter(valoracion_usuario = None).all()
    return render(request, "examen/usuario_sin.html", {"usuario_sin":puntos})

#Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el propietario tenga un nombre que contenga un texto en concreto, por ejemplo “Juan”

def cuentas_bancos(request, nombre):
    cuentas = (CuentaBancaria.objects.select_related("usuario")).all()
    cuentas = cuentas.filter(Q(banco = "CA")|Q(banco = "UC")).filter(usuario__nombre__contains = nombre)
    return render(request, "examen/banco.html", {"bancos_nombre":cuentas})


#Obtener todos los modelos principales que tengan una media de votaciones mayor del 2,5.

def modelos_con_media_mayor_2_5(request):
    modelos_moto = Moto.objects.annotate(media_puntuacion=Avg('valoracion_moto__puntuacion')).filter(media_puntuacion__gt=2.5)
    return render(request, "examen/media.html", {"motos": modelos_moto})


    
#formularios

def moto_create(request):
    # Si la petición es GET se creará el formulario Vacío
    # Si la petición es POST se creará el formulario con Datos.
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
    
    #formulario = LibroForm(datosFormulario)
    formulario = MotoForm(datosFormulario)
    """formularioFactory = modelform_factory(Libro, 
                                            fields='__all__',
                                            widgets = {
                                                "fecha_publicacion":forms.SelectDateWidget()
                                            })
    formulario = formularioFactory(datosFormulario)"""
    
    if (request.method == "POST"):
        # Llamamos la función que creará el libro
        #libro_creado = crear_libro_generico(formulario)
        moto_creado = crear_moto_modelo(formulario)
        if(moto_creado):
             messages.success(request, 'Se ha creado la moto'+formulario.cleaned_data.get('nombre')+" correctamente")
             return redirect("lista_moto")
    return render(request,"motos/create.html", {"formulario_moto":formulario})

def crear_moto_modelo(formulario):
    moto_creado = False
    # Comprueba si el formulario es válido
    if formulario.is_valid():
        try:
            # Guarda el libro en la base de datos
            formulario.save()
            moto_creado = True
        except:
            pass
    return moto_creado






def concesionario_create(request):
    # Si la petición es GET se creará el formulario Vacío
    # Si la petición es POST se creará el formulario con Datos.
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
    
    #formulario = LibroForm(datosFormulario)
    formulario = ConcesionarioForm(datosFormulario)
    """formularioFactory = modelform_factory(Libro, 
                                            fields='__all__',
                                            widgets = {
                                                "fecha_publicacion":forms.SelectDateWidget()
                                            })
    formulario = formularioFactory(datosFormulario)"""
    
    if (request.method == "POST"):
        # Llamamos la función que creará el libro
        #libro_creado = crear_libro_generico(formulario)
        concesionario_creado = crear_concesionario_modelo(formulario)
        if(concesionario_creado):
             messages.success(request, 'Se ha creado el concesionario'+formulario.cleaned_data.get('nombre')+" correctamente")
             return redirect("concesionario_lista")
    return render(request,"concesionario/create.html", {"formulario_concesionario":formulario})

def crear_concesionario_modelo(formulario):
    concesionario_creado = False
    # Comprueba si el formulario es válido
    if formulario.is_valid():
        try:
            # Guarda el libro en la base de datos
            formulario.save()
            concesionario_creado = True
        except:
            pass
    return concesionario_creado




