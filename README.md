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

