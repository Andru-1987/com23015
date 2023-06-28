from .models import Vino

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView , CreateView , UpdateView

# Create your views here.


class VinosBaseView(View):
    """
    Clase abstracta general
    """
    
    template_name = "pages/vinos.html"
    model = Vino
    fields = "__all__"
    sucess_url = reverse_lazy("vinos:all")
    



class VinosListView(VinosBaseView,ListView):
    """
    Muestra todos los vinos
    """

class VinosDetailView(VinosBaseView,DetailView):
    template_name = "pages/vino_detail.html"
    success_url = reverse_lazy("vinos:all")

class VinosCreateView(VinosBaseView,CreateView):
    template_name = "pages/vino_crear.html"
    success_url = reverse_lazy("vinos:all")
    extra_context = {
        "tipo" : "CREAR VINO"
    }
    

class VinosUpdateView(VinosBaseView,UpdateView):
    template_name = "pages/vino_crear.html"
    extra_context = {
        "tipo" : "ACTUALIZAR VINO"
    }
    success_url = reverse_lazy("vinos:all")
    
    

class VinosDeleteView(VinosBaseView,DeleteView):
    template_name = "pages/vino_delete.html"
    extra_context = {
        "tipo" : "BORRAR VINO"
    }
    success_url = reverse_lazy("vinos:all")