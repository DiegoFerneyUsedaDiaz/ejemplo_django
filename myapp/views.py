from django.http import JsonResponse
from django.shortcuts import render
from .models import CentroComercial, Tienda
from django.contrib.auth.models import User

# Create your views here.
def lista_centros_comerciales(request):
    centros_comerciales = CentroComercial.objects.all()
    return render(request, 'lista_centros_comerciales.html', {'centros_comerciales': centros_comerciales})

def lista_centros_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'lista_tiendas.html', {'tiendas': tiendas})

def vista_centros_comercial(request, name_cc):
    centro_comercial = CentroComercial.objects.get(nombre=name_cc)
    tiendas = centro_comercial.tiendas.all()
    return render(request, 'vista_centros_comercial.html', {'centro_comercial': centro_comercial, 'tiendas': tiendas})

def profile(request):
    if request.method == 'POST':
        data= request.POST
        new_name1 = data.get('first_name')
        new_name2 = data.get('last_name')
        new_email = data.get('email')
        
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user.first_name = new_name1
        user.last_name = new_name2
        user.email = new_email 
        user.save()
        return JsonResponse({'status': 'success'})
        
    return render(request, 'usuario.html')
        
        
