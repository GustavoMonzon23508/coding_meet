from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'], email=request.POST['EmailField'])
                user.save()
                return redirect ('Eventos')
            except:
                return render(request, 'signup.html', {
                     'form': UserCreationForm,
                     "error": 'Usuario ya existe' })                                                  
    return render(request, 'signup.html', {
                     'form': UserCreationForm,
                     "error": 'Las contraseñas no coinciden' })                                                  
       


def eventos(request):
    return render(request, 'eventos.html')


"""
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if (request, username=request.POST['username'], password=request.POST['password1'])
        return render(request, 'signin.html', {
        'form': AuthenticationForm
    })
    else:
        user=authenticate(
            request, username=request.POST['username'], password=request.POST['password1'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'nombre usuario o contraseña incorrecta'})
        else:
            login(request, user)
            return redirect('eventos')
           
      
        
"""
