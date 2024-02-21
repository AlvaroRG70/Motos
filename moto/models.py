from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
class UsuarioLogin(AbstractUser):
    TRABAJADOR = 1
    CLIENTE = 2
    ROLES = (
        (TRABAJADOR, 'trabajador'),
        (CLIENTE, 'cliente'),
    )
    
    rol  = models.PositiveSmallIntegerField(
        choices=ROLES,default=1
    )
    

from automatic_crud.models import BaseModel
# Create your models here.


class UploadedFile(models.Model):
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uploaded_on.date()

class Usuario(BaseModel):
    nombre = models.CharField(max_length=50)

    apellidos = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100, unique=True, blank=True)
    contraseña = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateTimeField(default=timezone.now)
    preferencias = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
    
class cliente(models.Model):
    usuario = models.OneToOneField(UsuarioLogin, on_delete=models.CASCADE, related_name='cliente_rel', unique=True)  


class Moto(BaseModel):
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
    imagen = models.FileField(default=None,blank=True)

    usuario = models.ManyToManyField(Usuario, through="VentaMoto", related_name="moto_vendida")
    comentador = models.ManyToManyField(Usuario, through="ValoracionMoto", related_name="moto_comentada")
    
    def __str__(self):
        return self.nombre

class DatosTecnicosMoto(BaseModel):
    num_serie = models.IntegerField(unique=True, blank=True)
    cilindrada = models.IntegerField()
    potencia = models.IntegerField()
    velocidad_maxima = models.IntegerField()
    tipo_motor = models.CharField(max_length=50)
    consumo = models.FloatField()
    sistema_frenado = models.CharField(max_length=50)
    moto = models.OneToOneField(Moto, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class AccesoriosMoto(BaseModel):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    def __str__(self):
        return self.nombre
    
class Boutique(BaseModel):
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
    def __str__(self):
        return self.nombre
    
class Concesionario(BaseModel):
    nombre = models.CharField(max_length=50)
    ubicacion = models.TextField()
    telefono = models.IntegerField(unique=True, blank=True)
    fecha_apertura = models.DateField()
    descripcion = models.TextField()
    moto = models.ManyToManyField(Moto, through="VentaConcesionario")
    def __str__(self):
        return self.nombre
    

class Taller(BaseModel):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(unique=True, blank=True)
    concesionario = models.OneToOneField(Concesionario, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class TrabajadorLogin(BaseModel):
    usuario = models.OneToOneField(UsuarioLogin, on_delete = models.CASCADE)

class Trabajador(BaseModel):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100, unique=True, blank=True)
    contraseña = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE, related_name="trabajador_concesionario")
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE, related_name="trabajador_taller")
    usuario = models.OneToOneField(UsuarioLogin, on_delete = models.CASCADE)


    def __str__(self):
        return self.nombre


    
class Evento(BaseModel):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=50)
    descripcion = models.TextField()
    kms = models.FloatField()
    usuario = models.ManyToManyField(Usuario, through="ReservaEvento", related_name = "reserva_evento")
    def __str__(self):
        return self.nombre
    

class VentaMoto(BaseModel):
    datos_compra = models.CharField(max_length=50)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="ventamoto_moto")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="ventamoto_usuario")
    def __str__(self):
        return self.nombre
    
class VentaConcesionario(BaseModel):
    datos = models.CharField(max_length=50)
    concesionario = models.ForeignKey(Concesionario, on_delete=models.CASCADE, related_name="ventaconc_concesionario")
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="ventaconc_moto")
    def __str__(self):
        return self.nombre
    
class ReservaEvento(BaseModel):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="reservaevento_evento")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="reservaevento_usuario")
    fecha_reserva = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre
    
    
#creamos el modelo puntuacion

class ValoracionMoto(BaseModel):
    puntuacion = models.IntegerField(default=0)
    comentario = models.TextField()
    fecha_votacion = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="valoracion_usuario")
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, related_name="valoracion_moto")
    def __str__(self):
        return self.nombre
    

# creamos el modelo de cuenta bancaria

class CuentaBancaria(BaseModel):
    num_cuenta = models.CharField(max_length=20, unique=True, blank=True)
    BANCO = [
        ("CA","Caixa"),
        ("BB","BBVA"),
        ("UC","UNICAJA"),
        ("IN","ING"),
    ]
    banco = models.CharField(max_length=2, choices=BANCO)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="cuenta_usuario")



#examen formularios

class Promocion(BaseModel):
    
    nombre = models.CharField(max_length=20, unique=True, blank=True)
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descuento = models.IntegerField()
    fecha_fin = models.DateField()
    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(default=timezone.now,blank=True)
    

