from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError
from .forms import Tareasform
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST
                    ['password1'])
            user.save()
            login(request, user)
            return redirect ('signup')
        except IntegrityError:
            return render(request, 'signup.html', {
                     'form': UserCreationForm,
                     "error": 'Usuario ya existe' }) 
                                                
    return render(request, 'signup.html', {
        'form': UserCreationForm,
        "error": 'las contraseñas no coinciden'
    })  
                                                           

def eventos(request):
    return render(request, 'eventos.html')
def crea_evento(request):
    return render(request, 'crea_evento.html',{
        'form': Tareasform
    })
def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm
    })
    else:        
        return render(request, 'signin.html',{
            'form': AuthenticationForm        
        })
      
        

