from django.shortcuts import render,redirect
from .forms import RegistroForm,LoginForm
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Usuario

class RegistroView(CreateView):
    form_class=RegistroForm
    template_name="registro.html"
    success_url= reverse_lazy("home")
    def form_valid(self, form):
        form.instance.username = form.cleaned_data.get("email")
        response = super().form_valid(form)
        email= form.cleaned_data.get("email")
        password =form.cleaned_data.get("password1")
        user= authenticate(username=email,password=password)
        login(self.request,user=user)
        return response
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)
    
def LogoutView(request):
    logout(request)
    return redirect("home")
    
class LoginUserView(LoginView):
    form_class=LoginForm
    template_name="login.html"
    success_url= reverse_lazy("home")
    def get_success_url(self):
        return reverse_lazy("home")
    

class ActualizarUsuario(UpdateView):
    form_class=RegistroForm
    template_name="registro.html"
    success_url= reverse_lazy("home")

    def get_object(self, queryset = ...):
        user=Usuario.objects.filter(pk=self.request.user.id).first()
        return user
   

class EliminarUsuario(DeleteView):
    model=Usuario
    template_name='formulariodelete.html'

    success_url= reverse_lazy('home')


    
    
