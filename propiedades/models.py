from django.db import models


# TEMPORAL: si tu compañero ya subió Terreno a main, BORRA esta clase
# e importa/usa el modelo real (mismo nombre: Terreno).
class Terreno(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nombre


class Vivienda(models.Model):
    class Tipo(models.TextChoices):
        CASA = "casa", "Casa"
        DEPARTAMENTO = "departamento", "Departamento"

    # PROTECT: no se puede borrar un terreno que todavía tiene viviendas.
    terreno = models.ForeignKey(
        Terreno, on_delete=models.PROTECT, related_name="viviendas"
    )
    tipo = models.CharField(max_length=20, choices=Tipo.choices)
    # Número o nombre dentro del terreno: "Casa 12", "Depto 301"
    identificador = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["terreno", "identificador"]
        constraints = [
            # Una vivienda no puede repetirse dentro del mismo terreno
            models.UniqueConstraint(
                fields=["terreno", "identificador"],
                name="vivienda_unica_por_terreno",
            )
        ]

    def __str__(self):
        return f"{self.get_tipo_display()} {self.identificador} - {self.terreno}"