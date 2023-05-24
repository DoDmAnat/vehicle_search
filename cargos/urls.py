from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CargoViewSet

app_name = "cargos"

router = DefaultRouter()

router.register("cargos", CargoViewSet, basename="cargos")

urlpatterns = [
    path("", include(router.urls))
]
