from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

CHOICES_DISPONIBILIDAD = (('disponible', 'disponible'),           
                          ('no disponible','no disponible'),
                          ('reservado', 'reservado'))  

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    resumen = models.CharField(max_length=500)
    rating = models.CharField(max_length=1)
    disponibilidad = models.CharField(default=True, max_length=20, choices=CHOICES_DISPONIBILIDAD)
    genero = models.CharField(max_length=200)
    fechaPublicacion= models.DateField()
    def marcar_como_reservado(self):
        self.disponibilidad = 'reservado'
        self.save()
           
class Editorial(models.Model):
    idEditorial = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    sitioWeb = models.CharField(max_length=200)
    
class Prestamo(models.Model):
    idPrestamo = models.CharField(max_length=200)
    estadoPrestamo = models.CharField(max_length=200)
    fechaPrestamo = models.DateField
    fechaDevolucion = models.DateField
    
class Usuario(AbstractUser):
    dni = models.CharField(max_length=9)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9)
    
    def __str__(self):
        return str(self.dni)
    
class Autor(models.Model):
    idAutor = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    sitioWeb = models.CharField(max_length=200)
    imagenAutor = models.ImageField(upload_to='autores/', null=True, blank=True)         
       
