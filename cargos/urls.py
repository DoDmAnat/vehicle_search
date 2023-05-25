from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CargoViewSet, CarViewSet

app_name = "cargos"

router = DefaultRouter()

router.register("cargos", CargoViewSet)
router.register("cars", CarViewSet)

urlpatterns = [
    path("", include(router.urls))
]
