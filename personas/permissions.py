
from rest_framework.permissions import BasePermission, SAFE_METHODS


class PermisoPersona(BasePermission):

    message = "No tienes permisos para realizar esta operacion."

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        if request.method in SAFE_METHODS:
            return view.action == "retrieve"

        return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        return (
            request.method in SAFE_METHODS
            and obj.activo
            and obj.usuario_id == request.user.id
        )


class PermisoRelacionPersonal(BasePermission):

    message = "No tienes permisos para gestionar relaciones personales."

    def has_permission(self, request, view):

        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )
