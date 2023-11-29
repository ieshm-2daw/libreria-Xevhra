from django.contrib import admin
from django.urls import path, include
from .views import ListLibro, DetailBookView, UpdateBookView, CreateBookView

urlpatterns = [
    path('libros/', ListLibro.as_view(), name='listadoLibros'),
    path('libros/<int:pk>/', DetailBookView.as_view(), name='detalle_libro'),
    path('libros/editar/<int:pk>/', UpdateBookView.as_view(), name='editar_libro'),
    path('libros/nuevo/', CreateBookView.as_view(), name='create_libro'),
    
]
