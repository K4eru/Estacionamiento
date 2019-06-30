from .models import Cliente,Estacionamiento
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

def regstrar_estacionaiento(request):
    
    variables = {}
    if request.method=='POST':
        esta = Estacionamiento()
        esta.dueño = request.user
        esta.direccion = request.POST.get('txtdireccion') 
        esta.descripcion = request.POST.get('txtdescrpcion')
        esta.latitud = float(request.POST.get('txtlatitud'))
        esta.longitud = float(request.POST.get('txtlongitud'))

        esta.save()


        return render(request,'app/registro_estacionamiento.html',variables)
    return render(request,'app/registro_estacionamiento.html',variables)


def mapa(request):
    estacionamientos = Estacionamiento.objects.all()
    variables = {'estacionamientos':estacionamientos}
    return render(request,'app/mapa.html',variables)