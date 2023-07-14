from .forms import VehiculoForm
from .models import Vehiculo
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'inicio_sesion.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('http://127.0.0.1:8000') 


def index(request):
    return render(request,'index.html')


def index(request):
    images = [
        {'url': 'https://res.cloudinary.com/dwl5avsdj/image/upload/f_auto,q_auto/zgpfregfimjurjmkq5fh','marca': 'Fiat', 'modelo': 'Punto'},
        {'url': 'https://res.cloudinary.com/dwl5avsdj/image/upload/f_auto,q_auto/y6kkqlybvqteczog2lej', 'marca': 'Fiat', 'modelo': 'Furgoneta Ducato'},
        {'url': 'https://res.cloudinary.com/dwl5avsdj/image/upload/f_auto,q_auto/qg16wrwksfz5s7nkeaje', 'marca': 'Ford', 'modelo': 'F-150 Lightning'},
        {'url': 'https://res.cloudinary.com/dwl5avsdj/image/upload/f_auto,q_auto/yufekpbltyh4arb4prcz', 'marca': 'Toyota', 'modelo': '4Runner'},
        {'url': 'https://res.cloudinary.com/dwl5avsdj/image/upload/f_auto,q_auto/g63jvn6xrgtzfjs6egnv', 'marca': 'Chevrolet', 'modelo': 'Corvette'},
    ]

    for i in range(len(images)):
        images[i]['id'] = i + 1

    context = {
        'images': images,
    }

    return render(request, 'index.html', context)

def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data['password1']
            user = authenticate(request, username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('http://127.0.0.1:8000') 
    else:
        form = UserCreationForm()
    return render(request, 'crear_usuario.html', {'form': form})



@permission_required('vehiculos.visualizar_catalogo')
@login_required
def catalogo(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'catalogo.html', context)


def crear_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            # Realizar otras acciones si es necesario
            return render(request, 'exito.html')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo_add.html', {'form': form})



def detalle_vehiculo(request, vehiculo_id):
    vehiculo = Vehiculo.objects.get(id=vehiculo_id)
    context = {
        'vehiculo': vehiculo
    }
    return render(request, 'detalles.html', context)

