from django.contrib import admin
from .models import Usuario
from .models import Trabajador
from .models import Moto
from .models import DatosTecnicosMoto
from .models import AccesoriosMoto
from .models import Boutique
from .models import Concesionario
from .models import Taller
from .models import Evento
from .models import CompraMasReciente
from .models import VentaMoto
from .models import VentaConcesionario
from .models import ReservaEvento

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Trabajador)
admin.site.register(Moto)
admin.site.register(DatosTecnicosMoto)
admin.site.register(AccesoriosMoto)
admin.site.register(Boutique)
admin.site.register(Concesionario)
admin.site.register(Taller)
admin.site.register(Evento)
admin.site.register(CompraMasReciente)
admin.site.register(VentaMoto)
admin.site.register(VentaConcesionario)
admin.site.register(ReservaEvento)