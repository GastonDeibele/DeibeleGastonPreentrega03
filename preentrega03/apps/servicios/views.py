from django.shortcuts import render
from django.urls import reverse_lazy
from .form import ServiciosForms
from .models import Servicios
from django.views.generic import CreateView,ListView,DetailView

class ServiciosView(CreateView):
    model=Servicios
    form_class=ServiciosForms
    template_name= 'formularios.html'

    success_url= reverse_lazy('home')

class ServiciosUsuarioList(ListView):
    model=Servicios   
    template_name='lista.html'

    context_object_name="objects"
    def get_context_data(self, **kwargs):
        context_data= super().get_context_data(**kwargs)
        context_data["urldetail"]="detalleservicio"
        return context_data


    def get(self, request, *args, **kwargs):
        inputuser = self.request.GET.get("input_name", "")
        queryset = self.get_queryset().filter(cliente__icontains=inputuser) 
        self.queryset=queryset
        
        return super().get(request, *args, **kwargs)
    
class ServicioDetallesList(DetailView):
    model=Servicios
    template_name='detalleservicio.html'

    context_object_name="servicio"