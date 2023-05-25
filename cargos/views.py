from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from .models import Cargo, Location, Car
from .serializers import (CargoSerializer, CargoCreateSerializer,
                          CargoUpdateSerializer)
from .utils import get_nearest_cars


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CargoSerializer
        if self.request.method == 'PUT':
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

    # def retrieve(self, request, pk=None):
    #     cargo = self.get_object()
    #     serializer = self.get_serializer(cargo)
    #
    #     # Получение списка номеров всех машин и их расстояний до выбранного груза
    #     cars = Car.objects.all()
    #     car_distances = []
    #     for car in cars:
    #         distance = geodesic(
    #             (
    #             car.current_location.latitude, car.current_location.longitude),
    #             (cargo.pick_up_location.latitude,
    #              cargo.pick_up_location.longitude)
    #         ).miles
    #         car_distances.append({
    #             'number': car.number,
    #             'distance': distance
    #         })
    #
    #     cargo_data = serializer.data
    #     cargo_data['car_distances'] = car_distances
    #
    #     return Response(cargo_data)
    #
    def update(self, request, pk=None):
        cargo = self.get_object()
        serializer = self.get_serializer(cargo, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     cargo = self.get_object()
    #     self.perform_destroy(cargo)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
