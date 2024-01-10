from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views import View
from typing import Any
from .models import Libro, Editorial, Autor, Prestamo, Usuario
from django.contrib.auth.mixins import LoginRequiredMixin


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
    paginate_by = 2
    
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["libros_disponibles"] = Libro.objects.filter(
            disponibilidad = 'disponible')
        context["libros_prestados"] = Libro.objects.filter(
            disponibilidad = 'no disponible')
        context["libros_reservados"] = Libro.objects.filter(
            disponibilidad = 'reservado')
        
        return context
    
    
class ListLibroPrestados (ListView):
    model = Libro
    template_name = 'libros/libros_prestados.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["libros_prestados"] = Libro.objects.filter(
            disponibilidad = 'no disponible')
        
        return context
    
class ListLibroReservados(ListView):
    model = Libro
    template_name = 'libros/libros_reservados.html'
    context_object_name = 'libros_reservados'


    # Aquí obtienes los Libros
    def get_queryset(self):
        queryset = Libro.objects.filter(disponibilidad='reservado')
        return queryset

    # Aquí los estas filtrando, como arriba
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libros_disponibles"] = Libro.objects.filter(disponibilidad='disponible')
        context["libros_prestados"] = Libro.objects.filter(disponibilidad='no disponible')
        return context           

class MarcarReservadoView(View):
    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        libro.marcar_como_reservado()
        return redirect('confirmar_reserva', pk=libro.pk)
    
    
class ConfirmarReservaView(View):
    def get(self, request, pk):
        # Aquí obtenemos el libro reservado
        libro = get_object_or_404(Libro, pk=pk)
        # Renderizar la página de confirmación con el libro
        return render(request, 'libros/reserva_confirmada.html', {'libro': libro})       

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
    

class CreateBookView(LoginRequiredMixin, CreateView):
    model = Libro
    template_name = 'libros/Create_Libro.html'
    fields = ['titulo', 'ISBN', 'portada', 'resumen',
              'disponibilidad', 'genero', 'rating', 'fechaPublicacion'] 
    success_url = reverse_lazy('listadoLibros')
    
    def form_valid(self, form):
        # Antes de guardar el formulario, marca el libro como reservado
        libro = form.save(commit=False)
        libro.marcar_como_reservado()
        return super().form_valid(form)
    
class DeleteBookView(DeleteView):
    model = Libro
    success_url = reverse_lazy('listadoLibros')
    template_name = 'Libros/confirmacionborrado.html'               