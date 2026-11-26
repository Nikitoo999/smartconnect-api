from rest_framework.routers import DefaultRouter

from .views import ViviendaViewSet

router = DefaultRouter()
router.register("viviendas", ViviendaViewSet, basename="vivienda")

urlpatterns = router.urls