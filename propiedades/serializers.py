from rest_framework import serializers

from .models import Vivienda


class ViviendaSerializer(serializers.ModelSerializer):
    terreno_nombre = serializers.CharField(source="terreno.nombre", read_only=True)
    tipo_display = serializers.CharField(source="get_tipo_display", read_only=True)

    class Meta:
        model = Vivienda
        fields = [
            "id",
            "terreno",
            "terreno_nombre",
            "tipo",
            "tipo_display",
            "identificador",
            "descripcion",
        ]
        # Mensaje propio para el UniqueConstraint (terreno + identificador)
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Vivienda.objects.all(),
                fields=["terreno", "identificador"],
                message="Ya existe una vivienda con ese identificador en este terreno.",
            )
        ]

    def validate_identificador(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("El identificador no puede estar vacío.")
        return value