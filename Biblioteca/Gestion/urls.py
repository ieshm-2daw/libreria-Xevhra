from django.contrib import admin
from django.urls import path, include
from .views import ListLibro, DetailBookView, UpdateBookView, CreateBookView, DeleteBookView, ListLibroPrestados

urlpatterns = [
    path('', ListLibro.as_view(), name='listadoLibros'),
    path('libros/prestados', ListLibroPrestados.as_view(), name='librosPrestados'),
    path('libros/<int:pk>/', DetailBookView.as_view(), name='detalle_libro'),
    path('libros/editar/<int:pk>/', UpdateBookView.as_view(), name='editar_libro'),
    path('libros/nuevo/', CreateBookView.as_view(), name='create_libro'),
    path('libros/<pk>/delete/', DeleteBookView.as_view(), name='borrar_libro'),
    
]
