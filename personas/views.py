
from django.db.models.deletion import ProtectedError
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Persona, RelacionPersonal
from .serializers import (
    PersonaSerializer,
    RelacionPersonalSerializer
)


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all().order_by("id")
    serializer_class = PersonaSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)

        except ProtectedError:
            return Response(
                {
                    "error": (
                        "No se puede eliminar esta persona "
                        "porque tiene registros relacionados."
                    )
                },
                status=status.HTTP_409_CONFLICT
            )


class RelacionPersonalViewSet(viewsets.ModelViewSet):
    queryset = RelacionPersonal.objects.all().order_by("id")
    serializer_class = RelacionPersonalSerializer
