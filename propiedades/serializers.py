from rest_framework import serializers

from .models import PuntoAcceso, Vivienda


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

class PuntoAccesoSerializer(serializers.ModelSerializer):
    terreno_nombre = serializers.CharField(source="terreno.nombre", read_only=True)
    tipo_display = serializers.CharField(source="get_tipo_display", read_only=True)

    class Meta:
        model = PuntoAcceso
        fields = [
            "id",
            "terreno",
            "terreno_nombre",
            "nombre",
            "tipo",
            "tipo_display",
            "activo",
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=PuntoAcceso.objects.all(),
                fields=["terreno", "nombre"],
                message="Ya existe un punto de acceso con ese nombre en este terreno.",
            )
        ]

    def validate_nombre(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return value