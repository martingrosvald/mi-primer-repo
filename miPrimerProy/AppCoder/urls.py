from django.contrib import admin
from django.urls import path
from AppCoder.views import saludo, saludar_a, saludo_personalizado, calculo_imc
from AppCoder.views import listar_cursos, listar_estudiantes, mostrar_index


urlpatterns = [
    path('mi-pagina', mostrar_index),
    path('hola/', saludo),
    path('saludar/persona/<nombre>', saludar_a),
    path('saludo_personalizado/', saludo_personalizado),
    path('imc/', calculo_imc),
    path('listar_cursos/', listar_cursos),
    path('listar_estudiantes/', listar_estudiantes)
    ]