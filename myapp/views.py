from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Persona, Mascota, Venta, Producto, VentaProducto, ConsultaMedica
from django.shortcuts import get_object_or_404
from myapp .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')
#####################################################################

def reg_funcionarios(request):

    formulario = formulario_Funcionario(request.POST or None)
    

    if request.method == 'POST':
        print(request.POST)
        if formulario.is_valid:
            formulario.save()
            return redirect('funcionarios')


    return render(request, 'reg_funcionarios.html', {'Funcionario' : formulario})

#####################################################################

def reg_mascota(request): ##### toca corregir por que la vista de mascota esta con el html de historias
    formulario = formulario_Mascota(request.POST or None)
    formulariop = formulario_Persona(request.POST or None ,initial = {'tipo':3})

    if request.method == 'POST':
        print(request.POST)
        if formulario.is_valid:
            formulario.save()
            return redirect('mascotas')
            

    return render(request, 'reg_historias.html', {'Mascotaf' : formulario, 'fpersona' : formulariop})

#####################################################################

def reg_productos(request):
    formulario = formulario_producto(request.POST or None)

    if request.method == 'POST':
        print(request.POST)
        if formulario.is_valid:
            formulario.save()

            return redirect("productos")


    return render(request, 'reg_productos.html', {'Productos' : formulario})

#####################################################################

def reg_historias(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect("productos")
    
    return render(request, 'reg_productos.html')

#####################################################################
def registrar2(request):
    formulario = formulario_Mascota(request.POST or None)
    formulariop = formulario_Persona(request.POST or None ,initial = {'tipo':3})

    if request.method == 'POST':
        print(request.POST)
        if formulario.is_valid:
            formulario.save()
            # formulariop.save()


    return render(request, 'reg_historias.html', {'Mascotaf' : formulario, 'fpersona' : formulariop})




def vista(request):
    
    productos = Producto.objects.all()


    
    return render(request, 'vista.html', {'productos' : productos})