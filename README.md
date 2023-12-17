# Motos
la lista esta en:
moto/promocion_list.html

create:
    path("formulario/promocion", views.promocion_create, name="formulario_promocion")
    class PromocionForm
    promocion_create
    promocion/crear_promociones.html

read:
    path("formulario/promocion_busqueda", views.promocion_busqueda_avanzada, name="promocion_buscar"),
    class BusquedaAvanzadaPromocionForm
    promocion_busqueda_avanzada
    promocion/busqueda_promocion.html

update:
    path('formulario/promocion_editar/<int:promocion_id>',views.promocion_editar,name='promocion_editar'),
    promocion_editar
    promocion/actualizar_promocion.html

delete:
    ruta --> <a href="/automatic-crud/moto/promocion/logic-delete/2/">ELIMINAR</a>
    template --> moto/trabajador_confirm_delete.html


6 cruds


Moto
  
create:
    path("formulario/moto", views.moto_create, name="formulario_moto"),
    class MotoForm
    def moto_create
    motos/create.html

read:
    path('moto/buscar_avanzado/',views.moto_buscar_avanzado,name='moto_buscar_avanzado'),    
    class BusquedaAvanzadaMotoForm
    def moto_buscar_avanzado
    motos/busqueda_avanzada.html

update:
path('formulario/motos_editar/<int:moto_id>',views.moto_editar,name='moto_editar'), 
concesionario_create
    motos/actualizar_moto.html

delete:
    template -->[trabajador_confirm_delete.html](moto/templates/moto/moto_confirm_delete.html)


Concesionario

create:
    path("formulario/concesionario", views.concesionario_create, name="formulario_concesionario"),
class ConcesionarioForm(ModelForm):    
def concesionario_create
    concesionario/create.html

read:
    path("formulario/concesionario_busqueda", views.concesionario_busqueda_avanzada, name="concesionarios_buscar"),
    class BusquedaAvanzadaConcesionarioForm(ModelForm):
    def concesionario_busqueda_avanzada(request):
    concesionario/concesionario_busqueda.html

update:
    path('formulario/concesionario_editar/<int:concesionario_id>',views.concesionario_editar,name='concesionario_editar'),
    concesionario_editar
    concesionario/actualizar_concesionario.html

delete:
    template -->[Title](moto/templates/moto/concesionario_confirm_delete.html)


Articulos

create:
    path("formulario/articulo", views.artículo_create, name="formulario_articulo"),
class ArticuloForm   
def artículo_create
    boutique/crear_articulos.html
read:
    path("formulario/articulo_busqueda", views.articulo_busqueda_avanzada, name="articulos_buscar"),
    class BusquedaAvanzadaArticuloForm
    def articulo_busqueda_avanzada
    boutique/articulos_busqueda.html

update:
    path('formulario/articulo_editar/<int:articulo_id>',views.articulo_editar,name='articulo_editar'),
    articulo_editar
    boutique/actualizar_articulo.html

delete:
    template -->[Title](moto/templates/moto/boutique_confirm_delete.html)


Eventos

create:
        path("formulario/evento", views.evento_create, name="formulario_evento"),
class EventoForm
def evento_create
    evento/crear_eventos.html
read:
    path("formulario/evento_busqueda", views.evento_busqueda_avanzada, name="eventos_buscar"),
    class BusquedaAvanzadaEventoForm
    def evento_busqueda_avanzada
    moto/evento_list.html

update:
    path('formulario/evento_editar/<int:evento_id>',views.evento_editar,name='formulario_editar'),
    evento_editar
    evento/actualizar_evento.html

delete:
    template -->[Title](moto/templates/moto/moto_confirm_delete.html)


Usuarios

create:
    path("formulario/usuario", views.usuario_create, name="formulario_usuario"),
    class UsuarioForm
    def usuario_create
    usuario/crear_usuarios.html
read:
    path("formulario/usuario_busqueda", views.usuario_busqueda_avanzada, name="usuarios_buscar"),
    class BusquedaAvanzadaUsuarioForm
    def usuario_busqueda_avanzada
    usuario/busqueda_usuario.html

update:
    path('formulario/usuario_editar/<int:usuario_id>',views.usuario_editar,name='usuario_editar'),
    usuario_editar
    usuario/actualizar_usuario.html

delete:
    template -->[Title](moto/templates/moto/evento_confirm_delete.html)


Trabajador


create:
    path("formulario/trabajador", views.trabajador_create, name="formulario_trabajador"),
    class TrabajadorForm
    def trabajador_create
    trabajador/crear_trabajadores.html
read:
    path("formulario/trabajador_busqueda", views.trabajador_busqueda_avanzada, name="trabajador_buscar"),
    class BusquedaAvanzadaTrabajadorForm
    def trabajador_busqueda_avanzada
    trabajador/busqueda_trabajador.html

update:
    path('formulario/trabajador_editar/<int:trabajador_id>',views.trabajador_editar,name='trabajador_editar'),
    trabajador_editar
    trabajador/actualizar_trabajador.html

delete:
    template -->[Title](moto/templates/moto/trabajador_confirm_delete.html)


LOGIN

Puedes registrarte, conectarte y desconectarte  

usuario trabajador --> usuario: AlvaroRodr | contraseña: ordenador4 --> Puede crear, editar y eliminar 
usuario cliente --> usuario: JorgeProfesor2 | contraseña: ordenador4 --> No puede crear, editar y eliminar 


!!!!IMPORTANTE¡¡¡¡¡

