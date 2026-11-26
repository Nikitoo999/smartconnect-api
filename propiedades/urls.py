from rest_framework.routers import DefaultRouter

from .views import PuntoAccesoViewSet, ViviendaViewSet

router = DefaultRouter()
router.register("viviendas", ViviendaViewSet, basename="vivienda")
router.register("puntos-acceso", PuntoAccesoViewSet, basename="punto-acceso")

urlpatterns = router.urls