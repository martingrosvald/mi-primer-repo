from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from AppCoder.models import Curso, Estudiante
# Create your views here.

def saludo(request):

    fecha_hora_ahora= datetime.now()
    return HttpResponse (f"Hola mundo {fecha_hora_ahora}")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola cómo estas {nombre.capitalize()}")

def mostrar_index(request):
    return render(request, "AppCoder/index.html",{"mi_titulo": "Hola es mi primer website!!!"})

def saludo_personalizado (request):

    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]
    return render(request,"AppCoder/index0.html", context)

def calculo_imc(request):
    context = {
        "imc":0
    }

    if request.GET:
        peso= float(request.GET["peso"])
        altura = float(request.GET ["altura"])
        context["imc"] = peso / (altura**2)
    return render(request, "AppCoder/index2.html", context)

def listar_cursos(request):
    context= {}
    
    context["cursos"] = Curso.objects.all() #modelo
    return render(request, "AppCoder/lista_cursos.html", context) #template

def listar_estudiantes(request):
    context= {}
    context["estudiantes"] = Estudiante.objects.all()
    return render(request, "AppCoder/lista_estudiantes.html", context) #template
