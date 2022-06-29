from django.shortcuts import redirect, render
from .models import *
from .forms import *

def inicio(request):

    return render(request,'suikaapp/inicio.html',{})


def nuevo_cliente(request):

    if request.method == 'POST':

        formulario_nuevo_cliente = Nuevo_Cliente(request.POST)

        if formulario_nuevo_cliente.is_valid():

            informacion = formulario_nuevo_cliente.cleaned_data

            nuevo_cliente = Cliente(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], edad = informacion['edad'] )

            nuevo_cliente.save()

            return redirect('inicio')

        else:

            return redirect('nuevo_cliente')

    else:

        formulario_vacio = Nuevo_Cliente()

        return render(request, "suikaapp/nuevo_cliente.html", {'form': formulario_vacio})

    
def nuevo_gorro(request):

    if request.method == 'POST':

        formulario_nuevo_gorro = Nueva_Gorra(request.POST)

        if formulario_nuevo_gorro.is_valid():

            informacion = formulario_nuevo_gorro.cleaned_data

            nuevo_gorro = Gorra(bordado = informacion['bordado'], color = informacion['color'], precio = informacion['precio'] )

            nuevo_gorro.save()

            return redirect('nuevo_gorro')

        else:

            return redirect('nuevo_gorro')

    else:

        formulario_vacio = Nueva_Gorra()

        return render(request, "suikaapp/nuevo_gorro.html", {'form': formulario_vacio})


def nueva_remera(request):



    if request.method == 'POST':

        formulario_nueva_remera = Nueva_Remera(request.POST)

        if formulario_nueva_remera.is_valid():

            informacion = formulario_nueva_remera.cleaned_data

            nueva_remera = Remera(color = informacion['color'], estampado = informacion['estampado'], talle = informacion['talle'], precio = informacion['precio'] )

            nueva_remera.save()

            return redirect('inicio')

        else:

            return redirect('nueva_remera')

    else:

        formulario_vacio = Nueva_Remera()

        return render(request, "suikaapp/nueva_remera.html", {'form': formulario_vacio})


def clientes(request):

    clientes = Cliente.objects.all()

    ctx = {'clientes': clientes}

    return render(request, "suikaapp/clientes.html", ctx)


def buscar_gorra(request):

    if request.method == 'POST':

        gorra = request.POST['gorra']

        gorras = Gorra.objects.filter(color__icontains = gorra)

        return render(request, 'suikaapp/buscar_gorra.html', {'gorras': gorras})

    else:

        gorras = []

        return render(request, 'suikaapp/buscar_gorra.html', {'gorras': gorras})


def buscar_cliente(request):

    if request.method == 'POST':

        cliente = request.POST['cliente']

        clientes = Cliente.objects.filter(nombre__icontains = cliente)

        return render(request, 'suikaapp/buscar_cliente.html', {'clientes': clientes})

    else:

        clientes = []

        return render(request, 'suikaapp/buscar_cliente.html', {'clientes': clientes})


def buscar_remera(request):

    if request.method == 'POST':

        remera = request.POST['remera']

        remeras = Remera.objects.filter(color__icontains = remera)

        return render(request, 'suikaapp/buscar_remera.html', {'remeras': remeras})

    else:

        remeras = []

        return render(request, 'suikaapp/buscar_remera.html', {'remeras': remeras})