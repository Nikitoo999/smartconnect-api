
from django.contrib import admin
from .models import Persona, RelacionPersonal


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "identificador",
        "nombre",
        "apellido",
        "usuario",
        "activo"
    )

    search_fields = (
        "identificador",
        "nombre",
        "apellido",
        "correo",
        "usuario__username"
    )

    list_filter = ("activo",)

    readonly_fields = ("fecha_registro",)

    ordering = ("id",)


@admin.register(RelacionPersonal)
class RelacionPersonalAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "persona_origen",
        "persona_destino",
        "tipo_relacion",
        "activa"
    )

    list_filter = (
        "tipo_relacion",
        "activa"
    )

    search_fields = (
        "persona_origen__nombre",
        "persona_destino__nombre"
    )

    ordering = ("id",)
