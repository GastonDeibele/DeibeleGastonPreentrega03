from django.shortcuts import render
from django.urls import reverse_lazy
from .form import RepuestosForms
from .models import Repuestos
from django.views.generic import CreateView,ListView


class RepuestosView(CreateView):
    model=Repuestos
    form_class=RepuestosForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')

class RepuestosUsuarioList(ListView):
    model=Repuestos   
    template_name='lista.html'

    context_object_name="objects"