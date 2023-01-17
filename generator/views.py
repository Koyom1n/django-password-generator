from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request, template_name='generator/home.html'):
    return render(request, template_name)


def password(request, template_name='generator/password.html'):
    
    try:
        caracteres = list("abcdefghijklmnopqrstuvwxyz")
        
        if request.GET.get('mayusculas'):
            caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
        if request.GET.get('especiales'):
            caracteres.extend(list('~!@#$%&()=|?<>+/*-_^.:;'))
        
        if request.GET.get('numeros'):
            caracteres.extend(list('0123456789'))
        
        lenght = int(request.GET.get('longitud'))
        
        contrasena = ''
        
        for x in range(lenght):
            contrasena += random.choice(caracteres)
        
        dato = {'pass': contrasena}
    except:
        contrasena = 'ERROR: Selecciona una opción para generar la contraseña'
    
    return render(request, template_name, dato)


def about(request, template_name='generator/about.html'):
    return render(request, template_name)


