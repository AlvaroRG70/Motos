from django.db import models
from django.utils import timezone
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100, unique=True, blank=True)
    contraseña = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateTimeField(default=timezone.now)
    preferencias = models.CharField(max_length=100)

    
class Moto(models.Model):
    nombre = models.CharField(max_length=50)
    MARCA = [
        ("KA","Kawasaki"),
        ("YA","Yamaha"),
        ("DU","Ducati"),
        ("HO","Honda"),
        ("BM","BMW"),
        ("TR","Triumph"),
        ("SZ","Suzuki"),
        ("KT","KTM"),
    ]
    marca = models.CharField(max_length=2, choices=MARCA)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    precio = models.FloatField()
    usuario = models.ManyToManyField(Usuario, through="VentaMoto", related_name="moto_vendida")
    comentador = models.ManyToManyField(Usuario, through="ValoracionMoto", related_name="moto_comentada")

class DatosTecnicosMoto(models.Model):
    num_serie = models.IntegerField(unique=True, blank=True)
    cilindrada = models.IntegerField()
    potencia = models.IntegerField()
    velocidad_maxima = models.IntegerField()
    tipo_motor = models.CharField(max_length=50)
    consumo = models.FloatField()
    sistema_frenado = models.CharField(max_length=50)
    moto = models.OneToOneField(Moto, on_delete=models.CASCADE)

class AccesoriosMoto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    
class Boutique(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    TALLA = [
        ("XS","xsmall"),
        ("SS","Small"),
        ("MM","Medium"),
        ("LL","Long"),
        ("XL","Xlong"),
    ]
    talla = models.CharField(max_length=2, choices=TALLA)
    stock = models.IntegerField(default=None)
    
class Concesionario(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.TextField()
    telefono = models.IntegerField(unique=True, blank=True)
    fecha_apertura = models.DateField()
    descripcion = models.TextField()
    moto = models.ManyToManyField(Moto, through="VentaConcesionario")
    

class Taller(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(unique=True, blank=True)
    concesionario = models.OneToOneField(Concesionario, on_delete=models.CASCADE)

class Trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100, unique=True, blank=True)
    contraseña = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE, related_name = "trabajador_concesionario")
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, related_name="trabajador_taller")


    
class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=50)
    descripcion = models.TextField()
    usuario = models.ManyToManyField(Usuario, through="ReservaEvento", related_name = "reserva_evento")
    

class VentaMoto(models.Model):
    datos_compra = models.CharField(max_length=50)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="ventamoto_moto")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="ventamoto_usuario")
    
class VentaConcesionario(models.Model):
    datos = models.CharField(max_length=50)
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE, related_name="ventaconc_concesionario")
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="ventaconc_moto")
    
class ReservaEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="reservaevento_evento")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="reservaevento_usuario")
    fecha_reserva = models.DateTimeField(default=timezone.now)
    
    
#creamos el modelo puntuacion

class ValoracionMoto(models.Model):
    puntuacion = models.IntegerField(default=0)
    comentario = models.TextField()
    fecha_votacion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="valoracion_usuario")
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="valoracion_moto")
    

# creamos el modelo de cuenta bancaria

class CuentaBancaria(models.Model):
    num_cuenta = models.CharField(max_length=20, unique=True, blank=True)
    BANCO = [
        ("CA","Caixa"),
        ("BB","BBVA"),
        ("UC","UNICAJA"),
        ("IN","ING"),
    ]
    banco = models.CharField(max_length=2, choices=BANCO)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cuenta_usuario")