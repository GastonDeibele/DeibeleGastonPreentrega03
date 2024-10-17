from django.contrib import admin

from .models import Servicios


class ServiciosAdmin(admin.ModelAdmin):

    model=Servicios

admin.site.register(Servicios,ServiciosAdmin)



# Register your models here.
