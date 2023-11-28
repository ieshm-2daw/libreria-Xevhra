from django.contrib import admin
from django.urls import path, include
from .views import listaLibros, listaUsuarios

urlpatterns = [
    path('', listaLibros, name='listadoLibros'),
    path('listadoUsuarios', listaUsuarios, name='listaUsuarios' ),
    
]
