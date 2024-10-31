from django.urls import path 
from .views import RegistroView, LogoutView,LoginUserView

urlpatterns = [
    path('',RegistroView.as_view(),name='formularioregistro'),
    path('logout/',LogoutView,name='logout'),
    path('login/',LoginUserView.as_view(),name='login')

]
