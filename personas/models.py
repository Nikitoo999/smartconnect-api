from django.db import models


from django.db import models


class Persona(models.Model):
    identificador = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "persona"
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class RelacionPersonal(models.Model):

    class TipoRelacion(models.TextChoices):
        PADRE = "PADRE", "Padre"
        MADRE = "MADRE", "Madre"
        HIJO = "HIJO", "Hijo"
        HIJA = "HIJA", "Hija"
        PAREJA = "PAREJA", "Pareja"
        HERMANO = "HERMANO", "Hermano"
        HERMANA = "HERMANA", "Hermana"
        TUTOR = "TUTOR", "Tutor legal"
        OTRO = "OTRO", "Otro"

    persona_origen = models.ForeignKey(
        Persona,
        on_delete=models.PROTECT,
        related_name="relaciones_origen"
    )

    persona_destino = models.ForeignKey(
        Persona,
        on_delete=models.PROTECT,
        related_name="relaciones_destino"
    )

    tipo_relacion = models.CharField(
        max_length=20,
        choices=TipoRelacion.choices
    )

    activa = models.BooleanField(default=True)

    class Meta:
        db_table = "relacion_personal"
        verbose_name = "Relacion personal"
        verbose_name_plural = "Relaciones personales"

        constraints = [
            models.CheckConstraint(
                check=~models.Q(
                    persona_origen=models.F("persona_destino")
                ),
                name="evitar_autorrelacion"
            ),
            models.UniqueConstraint(
                fields=[
                    "persona_origen",
                    "persona_destino",
                    "tipo_relacion"
                ],
                name="relacion_personal_unica"
            )
        ]

    def __str__(self):
        return (
            f"{self.persona_origen} - "
            f"{self.tipo_relacion} - "
            f"{self.persona_destino}"
        )

