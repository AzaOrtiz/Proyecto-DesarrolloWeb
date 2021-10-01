from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name='index.html'

class StoreView (TemplateView):
    template_name='tienda.html'

class ProductosView (TemplateView):
    template_name='producto.html'

class PagarView (TemplateView):
    template_name='pagar.html'

class BlankView (TemplateView):
    template_name='blank.html'