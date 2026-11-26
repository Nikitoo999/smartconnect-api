from django.db.models import ProtectedError
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import PuntoAcceso, Vivienda
from .serializers import PuntoAccesoSerializer, ViviendaSerializer


class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.select_related("terreno").all()
    serializer_class = ViviendaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtros opcionales: /api/viviendas/?terreno=1&tipo=casa
        qs = super().get_queryset()
        terreno = self.request.query_params.get("terreno")
        tipo = self.request.query_params.get("tipo")
        if terreno:
            qs = qs.filter(terreno_id=terreno)
        if tipo:
            qs = qs.filter(tipo=tipo)
        return qs

    def destroy(self, request, *args, **kwargs):
        # Cuando existan asignaciones Persona-Vivienda con on_delete=PROTECT,
        # esto devuelve 409 en vez de un error 500.
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {"detail": "No se puede eliminar: la vivienda tiene relaciones asociadas."},
                status=status.HTTP_409_CONFLICT,
            )

class PuntoAccesoViewSet(viewsets.ModelViewSet):
    queryset = PuntoAcceso.objects.select_related("terreno").all()
    serializer_class = PuntoAccesoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtros opcionales: /api/puntos-acceso/?terreno=1&tipo=porton&activo=true
        qs = super().get_queryset()
        terreno = self.request.query_params.get("terreno")
        tipo = self.request.query_params.get("tipo")
        activo = self.request.query_params.get("activo")
        if terreno:
            qs = qs.filter(terreno_id=terreno)
        if tipo:
            qs = qs.filter(tipo=tipo)
        if activo is not None:
            qs = qs.filter(activo=activo.lower() == "true")
        return qs

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {"detail": "No se puede eliminar: el punto de acceso tiene relaciones asociadas."},
                status=status.HTTP_409_CONFLICT,
            )