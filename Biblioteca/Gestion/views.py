from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views import View
from typing import Any
from .models import Libro, Editorial, Autor, Prestamo, Usuario


# Create your views here.
# def listaLibros(request, template_name='Lista.html'):
#    libros = Libro.objects.all()
#    return render(request, template_name, {'libros': libros})

# def listaUsuarios(request):
#    usuarios = Usuario.objects.all()
#    return render(request, 'listadoUsuarios.html', {'usuarios ': usuarios})

# ListView, CreateView, DetailView, DeleteView


class ListLibro (ListView):
    model = Libro
    template_name = 'libros/Lista.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["libros_disponibles"] = Libro.objects.filter(
            disponibilidad = 'disponible')
        context["libros_prestados"] = Libro.objects.filter(
            disponibilidad = 'no disponible')
        
        return context
    
    
class ListLibroPrestados (ListView):
    model = Libro
    template_name = 'libros/libros_prestados.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["libros_prestados"] = Libro.objects.filter(
            disponibilidad = 'no disponible')
        
        return context    
    

class DetailBookView(DetailView):
    model = Libro
    template_name = 'libros/libro_detail.html'  
    context_object_name = 'libro'
    
class UpdateBookView(UpdateView):
    model = Libro
    template_name = 'libros/editar_Libro.html'
    fields = ['titulo', 'ISBN', 'portada', 'resumen',
              'disponibilidad', 'genero', 'rating', 'fechaPublicacion']
    success_url = reverse_lazy('listadoLibros')
    

class CreateBookView(CreateView):
    model = Libro
    template_name = 'libros/Create_Libro.html'
    fields = ['titulo', 'ISBN', 'portada', 'resumen',
              'disponibilidad', 'genero', 'rating', 'fechaPublicacion'] 
    success_url = reverse_lazy('listadoLibros')
    
class DeleteBookView(DeleteView):
    model = Libro
    success_url = reverse_lazy('listadoLibros')
    template_name = 'Libros/confirmacionborrado.html'               