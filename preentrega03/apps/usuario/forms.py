from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import Usuario

class LoginForm(AuthenticationForm):
    class Meta:
        model = Usuario
        
class RegistroForm(UserCreationForm):
    class Meta:
        model= Usuario
        fields= ["first_name","last_name","email","password1","password2"]
