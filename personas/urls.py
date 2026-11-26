
from rest_framework.routers import DefaultRouter
from .views import PersonaViewSet, RelacionPersonalViewSet

router = DefaultRouter()

router.register(
    r"personas",
    PersonaViewSet,
    basename="persona"
)

router.register(
    r"relaciones-personales",
    RelacionPersonalViewSet,
    basename="relacion-personal"
)

urlpatterns = router.urls
