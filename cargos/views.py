from rest_framework import viewsets
from rest_framework.response import Response

from .models import Cargo, Car
from .serializers import (CargoSerializer, CargoCreateSerializer,
                          CargoUpdateSerializer, CarSerializer)
from .utils import get_nearest_cars, get_all_cars_distance


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CargoSerializer
        if self.request.method in ('PUT', 'PATCH'):
            return CargoUpdateSerializer
        return CargoCreateSerializer

    def list(self, request, *args, **kwargs):
        cargos = self.get_queryset()
        serializer = self.get_serializer(cargos, many=True)
        data = serializer.data

        cars = Car.objects.all()

        for cargo in data:
            cargo_obj = Cargo.objects.get(id=cargo['id'])
            nearest_cars_count = get_nearest_cars(cargo_obj, cars)
            cargo['nearest_cars_count'] = nearest_cars_count

        return Response(data)

    def retrieve(self, request, pk=None):
        cargo = self.get_object()
        serializer = self.get_serializer(cargo)
        data = serializer.data

        cars = Car.objects.all()
        car_distances = get_all_cars_distance(cargo, cars)

        cargo_data = serializer.data
        cargo_data['car_distances'] = car_distances
        data['car_distances'] = car_distances

        return Response(data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
