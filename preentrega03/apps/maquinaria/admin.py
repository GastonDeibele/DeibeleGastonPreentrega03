from django.contrib import admin

from .models import Maquinaria


class MaquinariaAdmin(admin.ModelAdmin):

    model=Maquinaria

admin.site.register(Maquinaria,MaquinariaAdmin)


# Register your models here.
