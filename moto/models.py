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
    
    
class Trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100, unique=True, blank=True)
    contraseña = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    
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
    usuario = models.ManyToManyField(Usuario, through="VentaMoto")

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
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    moto = models.ManyToManyField(Moto, through="VentaConcesionario")

class Taller(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(unique=True, blank=True)
    concesionario = models.OneToOneField(Concesionario, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    
class Evento(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=50)
    descripcion = models.TextField()
    usuario = models.ManyToManyField(Usuario, through="ReservaEvento", related_name="reserva_evento")
    
class CompraMasReciente(models.Model):
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.FloatField()
    fecha_compra = models.DateTimeField(timezone.now)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class VentaMoto(models.Model):
    datos_compra = models.CharField(max_length=50)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
class VentaConcesionario(models.Model):
    datos = models.CharField(max_length=50)
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    
class ReservaEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(default=timezone.now)