from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def Agendar(request):
    return render(request, 'Agendar.html')

def Funcionarios(request):
    return render(request, 'Funcionarios.html')

def Paciente(request):
    return render(request, 'Paciente.html')

def Resumen(request):
    return render(request, 'Resumen.html')

def Productos(request):
    return render(request, 'Productos.html')

def Ventas(request):
    return render(request, 'Ventas.html')

def Historial_Cli(request):
    return render(request, 'Historial_cli.html')

