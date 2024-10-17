from django.contrib import admin

from .models import Repuestos


class RepuestosAdmin(admin.ModelAdmin):

    model=Repuestos

admin.site.register(Repuestos,RepuestosAdmin)



# Register your models here.
