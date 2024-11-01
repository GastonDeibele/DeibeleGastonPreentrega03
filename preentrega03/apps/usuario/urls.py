from django.urls import path 
from .views import RegistroView, LogoutView,LoginUserView,EliminarUsuario,ActualizarUsuario


urlpatterns = [
    path('',RegistroView.as_view(),name='formularioregistro'),
    path('logout/',LogoutView,name='logout'),
    path('login/',LoginUserView.as_view(),name='login'),
    path('actualizar/',ActualizarUsuario.as_view(),name='actualizarusuario'),
    path('eliminar/',EliminarUsuario.as_view(),name='eliminarusuario')

]
