from django.shortcuts import render
from django.urls import reverse_lazy
from .form import MaquinariaForms
from .models import Maquinaria
from django.views.generic import CreateView,ListView,DetailView,UpdateView, DeleteView


class MaquinariaView(CreateView):
    model=Maquinaria
    form_class=MaquinariaForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')

class MaquinariaUsuarioList(ListView):
    model=Maquinaria    
    template_name='lista.html'

    context_object_name="objects"
    def get_context_data(self, **kwargs):
        context_data= super().get_context_data(**kwargs)
        context_data["urldetail"]="detallemaquinaria"
        return context_data
    
    def get(self, request, *args, **kwargs):
        inputuser = self.request.GET.get("input_name", "")
        queryset = self.get_queryset().filter(marca__icontains=inputuser) 
        self.queryset=queryset
        
        return super().get(request, *args, **kwargs)

class MaquinariaDetallesList(DetailView):
    model=Maquinaria
    template_name='detallemaquinaria.html'

    context_object_name="maquinaria"

class ActualizarMaquinaria(UpdateView):
    model=Maquinaria
    form_class=MaquinariaForms
    template_name='formularios.html'

    success_url= reverse_lazy('home')


class EliminarMaquinaria(DeleteView):
    model=Maquinaria
    template_name='formulariodelete.html'

    success_url= reverse_lazy('home')


# Create your views here.
