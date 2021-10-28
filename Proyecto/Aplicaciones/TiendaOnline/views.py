from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from Aplicaciones.TiendaOnline.models import accesorio, imgMarcas
from Aplicaciones.TiendaOnline.models import computadora, accesorio
from Aplicaciones.TiendaOnline.Carrito import Carrito


# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class StoreView (TemplateView):
    template_name='computadoras.html'

class AccesoriosView (TemplateView):
    template_name='accesorios.html'

class PagarView (TemplateView):
    template_name='pagar.html'

class BlankView (TemplateView):
    template_name='blank.html'

def ListarComputadoras(request):
    productos = computadora.objects.all()
    return render(request, "computadoras.html", {'productos':productos})

def agregar_computadora(request, producto_id):
    carrito = Carrito(request)
    producto = computadora.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("pagar")

def eliminar_computadora(request, producto_id):
    carrito = Carrito(request)
    producto = computadora.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("pagar")

def restar_computadora(request, producto_id):
    carrito = Carrito(request)
    producto = computadora.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("pagar")

def limpiar_computadora(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("pagar")

#Accesorios******************************************************************************************

def ListarAccesorios(request): 
    accesorios = accesorio.objects.all()
    return render(request, "accesorios.html", {'accesorios':accesorios})

def agregar_accesorio(request, accesorio_id):
    carrito = Carrito(request)
    acces = accesorio.objects.get(id=accesorio_id)
    carrito.agregar(acces)
    return redirect("pagar")

def eliminar_accesorio(request, accesorio_id):
    carrito = Carrito(request)
    acces = accesorio.objects.get(id=accesorio_id)
    carrito.eliminar(acces)
    return redirect("pagar")

def restar_accesorio(request, accesorio_id):
    carrito = Carrito(request)
    acces = accesorio.objects.get(id=accesorio_id)
    carrito.restar(acces)
    return redirect("pagar")

def limpiar_accesorio(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("pagar")


class ListarImg(ListView):
    template_name= 'index.html'
    model = imgMarcas

    def get_queryset(self):
        return imgMarcas.objects.all()