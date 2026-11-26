from django.contrib import admin

from .models import Terreno, Vivienda


@admin.register(Terreno)
class TerrenoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "direccion")


@admin.register(Vivienda)
class ViviendaAdmin(admin.ModelAdmin):
    list_display = ("id", "terreno", "tipo", "identificador")
    list_filter = ("terreno", "tipo")
    search_fields = ("identificador",)
