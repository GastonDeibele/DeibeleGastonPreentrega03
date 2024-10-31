from django.shortcuts import render
from django.urls import reverse_lazy
from .form import MaquinariaForms
from .models import Maquinaria
from django.views.generic import CreateView,ListView


class MaquinariaView(CreateView):
    model=Maquinaria
    form_class=MaquinariaForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')

class MaquinariaUsuarioList(ListView):
    model=Maquinaria    
    template_name='lista.html'

    context_object_name="objects"



# Create your views here.
