from django.contrib import admin

# Register your models here.

from .models import Viaje, Cliente

admin.site.register(Viaje)
admin.site.register(Cliente)
