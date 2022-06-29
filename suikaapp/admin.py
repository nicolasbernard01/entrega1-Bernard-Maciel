from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'edad', 'email')

admin.site.register(Cliente, ClienteAdmin)


class GorraAdmin(admin.ModelAdmin):

    list_display = ('bordado', 'color', 'precio')

admin.site.register(Gorra, GorraAdmin)


class RemeraAdmin(admin.ModelAdmin):

    list_display = ('color', 'estampado', 'talle', 'precio')

admin.site.register(Remera, RemeraAdmin)

