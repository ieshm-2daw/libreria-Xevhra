from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    portada = models.CharField(max_length=200)
    resumen = models.CharField(max_length=500)
    disponibilidad = models.CharField(default=True, max_length=10)
    genero = models.CharField(max_length=200)
    fechaPublicacion= models.DateField()    
    
    
    
    
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
       
