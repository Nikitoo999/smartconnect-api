
from django.db.models.deletion import ProtectedError

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Persona, RelacionPersonal

from .serializers import (
    PersonaSerializer,
    RelacionPersonalSerializer
)

from .permissions import (
    PermisoPersona,
    PermisoRelacionPersonal
)


class PersonaViewSet(viewsets.ModelViewSet):

    queryset = Persona.objects.all().order_by("id")
    serializer_class = PersonaSerializer

    authentication_classes = [JWTAuthentication]

    permission_classes = [
        IsAuthenticated,
        PermisoPersona
    ]

    def destroy(self, request, *args, **kwargs):

        try:
            return super().destroy(
                request, *args, **kwargs
            )

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

    authentication_classes = [JWTAuthentication]

    permission_classes = [
        IsAuthenticated,
        PermisoRelacionPersonal
    ]
