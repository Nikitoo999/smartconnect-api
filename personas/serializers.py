
from datetime import date
from rest_framework import serializers
from .models import Persona, RelacionPersonal


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = [
            "id",
            "identificador",
            "nombre",
            "apellido",
            "fecha_nacimiento",
            "correo",
            "telefono",
            "activo",
            "fecha_registro"
        ]

        read_only_fields = ["id", "fecha_registro"]

    def validate_fecha_nacimiento(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "La fecha de nacimiento no puede ser futura."
            )
        return value


class RelacionPersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelacionPersonal
        fields = [
            "id",
            "persona_origen",
            "persona_destino",
            "tipo_relacion",
            "activa"
        ]

        read_only_fields = ["id"]

    def validate(self, data):
        origen = data.get(
            "persona_origen",
            getattr(self.instance, "persona_origen", None)
        )

        destino = data.get(
            "persona_destino",
            getattr(self.instance, "persona_destino", None)
        )

        if origen == destino:
            raise serializers.ValidationError(
                "Una persona no puede relacionarse consigo misma."
            )

        return data
