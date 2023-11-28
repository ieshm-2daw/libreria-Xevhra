from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from django.views import View
from .models import Libro, Editorial, Autor, Prestamo, Usuario


# Create your views here.
def listaLibros(request, template_name='Lista.html'):
    libros = Libro.objects.all()
    return render(request, template_name, {'libros': libros})

def listaUsuarios(request):
    usuarios = Usuario.objects.all()
    
    
    
    return render(request, 'listadoUsuarios.html', {'usuarios ': usuarios})