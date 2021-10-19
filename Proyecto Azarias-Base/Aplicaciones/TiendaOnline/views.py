from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from Aplicaciones.TiendaOnline.models import accesorio, computadora


# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class StoreView (TemplateView):
    template_name='computadoras.html'

class ProductosView (TemplateView):
    template_name='producto.html'

class PagarView (TemplateView):
    template_name='pagar.html'

class BlankView (TemplateView):
    template_name='blank.html'


class ListarComputadoras(ListView):
    template_name= 'computadoras.html'
    model = computadora

    def get_queryset(self):
        return computadora.objects.all()

class ListarAccesorios(ListView):
    template_name= 'index.html'
    model = accesorio

    def get_queryset(self):
        return accesorio.objects.all()