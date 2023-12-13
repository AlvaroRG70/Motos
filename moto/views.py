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

def eventos_listar(request):
    eventos = (Moto.objects.prefetch_related("usuario")).all()
    return render(request, "moto/evento_list.html", {"object_list":eventos})
    

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

#CRUD

#Crear moto

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

#BUSCAR

def moto_buscar(request):
    
    formulario = MotoBusquedaForm(request.GET)
    
    if formulario.is_valid():
        texto = formulario.cleaned_data.get('textoBusqueda')
        motos = Moto.objects.prefetch_related("usuario")
        motos = motos.filter(Q(nombre__contains=texto) | Q(modelo__contains=texto)).all()
        mensaje_busqueda = "Se buscar por motos que contienen en su nombre o modelo la palabra: "+texto
        return render(request, 'motos/motos_lista_busqueda.html',{"lista_moto":motos,"texto_busqueda":mensaje_busqueda})
    
    if("HTTP_REFERER" in request.META):
        return redirect(request.META["HTTP_REFERER"])
    else:
        return redirect("index")
    
#avanzada

def moto_buscar_avanzado(request):
    
    if (len(request.GET)>0):
        formulario = BusquedaAvanzadaMotoForm(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado por:\n"
            
            QSmotos = Moto.objects
            
            textoBusqueda=formulario.cleaned_data.get('textoBusqueda')
            marca = formulario.cleaned_data.get('marca')
            anyo = formulario.cleaned_data.get('anyo')
            precio = formulario.cleaned_data.get('precio')

            if textoBusqueda is not None:
                QSmotos = QSmotos.filter(Q(nombre__contains=textoBusqueda) | Q(marca__contains=textoBusqueda) | Q(modelo__contains=textoBusqueda))
                mensaje+=" Contiene: "+ textoBusqueda+"\n"
            
            if(len(marca)>0):
                mensaje +=" la marca sea "+marca[0]
                filtroOR = Q(marca=marca[0])
                for marca in marca[1:]:
                    mensaje += " o "+marca[1]
                    filtroOR |= Q(marca=marca)
                mensaje += "\n"
                QSmotos =  QSmotos.filter(filtroOR)
            
            if anyo is not None:
                QSmotos = QSmotos.filter(año__startswith=anyo)
                mensaje+= str(anyo)+"\n"
                
            if precio is not None:
                QSmotos = QSmotos.filter(precio__startswith=precio)
                mensaje+= str(precio)+"\n"
                
            
            motos = QSmotos.all()
            
            return render(request,'moto/moto_list.html',{"object_list":motos, "texto":mensaje})
    else:
        formulario = BusquedaAvanzadaMotoForm(None)
    return render(request,'motos/busqueda_avanzada.html',{"formulario":formulario})



#CRUD concesionario
def concesionario_create(request):
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST

    formulario = ConcesionarioForm(datosFormulario)
    
    if (request.method == "POST"):
        concesionario_creado = crear_concesionario_modelo(formulario)
        if(concesionario_creado):
             messages.success(request, 'Se ha creado el concesionario'+formulario.cleaned_data.get('nombre')+" correctamente")
             return redirect("moto-concesionario-list")
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


#busqueda avanzada

def concesionario_busqueda_avanzada(request):

    if (len(request.GET)>0):
        formulario = BusquedaAvanzadaConcesionarioForm(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado por:\n"
            
            QSconcesionario = Concesionario.objects
            
            textoBusqueda=formulario.cleaned_data.get('textoBusqueda')
            telefono=formulario.cleaned_data.get('telefono')

            if textoBusqueda is not None:
                QSconcesionario = QSconcesionario.filter(Q(nombre__contains=textoBusqueda) | Q(ubicacion__contains=textoBusqueda) | Q(descripcion__contains=textoBusqueda))
                mensaje+=" Contiene: "+ textoBusqueda+"\n"
            
            if telefono is not None:
                QSconcesionario = QSconcesionario.filter(telefono__startswith=telefono)
                mensaje+= str(telefono)+"\n"
            
            concesionario = QSconcesionario.all()
            
            return render(request,'moto/concesionario_list.html',{"object_list":concesionario, "texto":mensaje})
    else:
        formulario = BusquedaAvanzadaConcesionarioForm(None)
    return render(request,'concesionario/concesionario_busqueda.html',{"formulario":formulario})






#CRUD PARA ARTICULOS

#CREAR

def artículo_create(request):
    
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
        
    formulario = ArticuloForm(datosFormulario)
    if (request.method == "POST"):
        if formulario.is_valid():
            try:
                # Guarda el libro en la base de datos
                formulario.save()
                return redirect("moto-boutique-list")
            except Exception as error:
                print(error)
    
    return render(request, 'boutique/crear_articulos.html',{"formulario_articulo":formulario})  



def articulo_busqueda_avanzada(request):
    if (len(request.GET)>0):
        formulario = BusquedaAvanzadaArticuloForm(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado por:\n"
            
            QSarticulos = Boutique.objects
            
            textoBusqueda=formulario.cleaned_data.get('textoBusqueda')
            talla = formulario.cleaned_data.get('talla')
            stock = formulario.cleaned_data.get('stock')
            precio = formulario.cleaned_data.get('precio')

            if textoBusqueda is not None:
                QSarticulos = QSarticulos.filter(Q(nombre__contains=textoBusqueda) | Q(tipo__contains=textoBusqueda) | Q(descripcion__contains=textoBusqueda))
                mensaje+=" Contiene: "+ textoBusqueda+"\n"
            
            if(len(talla)>0):
                mensaje +=" la marca sea "+talla[0]
                filtroOR = Q(talla=talla[0])
                for talla in talla[1:]:
                    mensaje += " o "+talla[1]
                    filtroOR |= Q(talla=talla)
                mensaje += "\n"
                QSarticulos =  QSarticulos.filter(filtroOR)
            
            if stock is not None:
                QSarticulos = QSarticulos.filter(año__startswith=stock)
                mensaje+= str(stock)+"\n"
                
            if precio is not None:
                QSarticulos = QSarticulos.filter(precio__startswith=precio)
                mensaje+= str(precio)+"\n"
                
            
            articulos = QSarticulos.all()
            
            return render(request,'moto/boutique_list.html',{"object_list":articulos, "texto":mensaje})
    else:
        formulario = BusquedaAvanzadaArticuloForm(None)
    return render(request,'boutique/articulos_busqueda.html',{"formulario":formulario})
    


#CRUD PARA EVENTOS

#CREAR

def evento_create(request):
    
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
        
    formulario = EventoForm(datosFormulario)
    if (request.method == "POST"):
        if formulario.is_valid():
            try:
                # Guarda el libro en la base de datos
                formulario.save()
                return redirect("moto-evento-list")
            except Exception as error:
                print(error)
    
    return render(request, 'evento/crear_eventos.html',{"formulario_evento":formulario})  


def evento_busqueda_avanzada(request):

    if (len(request.GET)>0):
        formulario = BusquedaAvanzadaEventoForm(request.GET)
        if formulario.is_valid():
            mensaje="Se ha buscado por:\n"
            
            QSeventos = Evento.objects
            
            textoBusqueda=formulario.cleaned_data.get('textoBusqueda')

            if textoBusqueda is not None:
                QSeventos = QSeventos.filter(Q(nombre__contains=textoBusqueda) | Q(ubicacion__contains=textoBusqueda) | Q(descripcion__contains=textoBusqueda))
                mensaje+=" Contiene: "+ textoBusqueda+"\n"
            
            eventos = QSeventos.all()
            
            return render(request,'moto/evento_list.html',{"object_list":eventos, "texto":mensaje})
    else:
        formulario = BusquedaAvanzadaEventoForm(None)
    return render(request,'evento/busqueda_evento.html',{"formulario":formulario})


#CRUD USUARIOS 

def usuario_create(request):
    
    datosFormulario = None
    if request.method == "POST":
        datosFormulario = request.POST
        
    formulario = UsuarioForm(datosFormulario)
    if (request.method == "POST"):
        if formulario.is_valid():
            try:
                # Guarda el libro en la base de datos
                formulario.save()
                return redirect("moto-usuario-list")
            except Exception as error:
                print(error)
    
    return render(request, 'usuario/crear_usuarios.html',{"formulario_usuario":formulario})