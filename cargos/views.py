from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from .models import Cargo, Location, Car
from .serializers import CargoSerializer, CargoCreateSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def create(self, request, *args, **kwargs):
        serializer = CargoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     # Получение списка грузов с локациями pick-up и delivery
    #     serializer = self.get_serializer(queryset, many=True)
    #     cargos_data = serializer.data
    #
    #     # Добавление количества ближайших машин до груза ( =< 450 миль)
    #     for cargo_data in cargos_data:
    #         pick_up_location = Location.objects.get(
    #             pk=cargo_data['pick_up_location'])
    #         num_close_cars = Car.objects.filter(
    #             current_location__distance_lte=(
    #             pick_up_location.point, D(mi=450))
    #         ).count()
    #         cargo_data['num_close_cars'] = num_close_cars
    #
    #     return Response(cargos_data)

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
    # def update(self, request, pk=None):
    #     cargo = self.get_object()
    #     serializer = self.get_serializer(cargo, data=request.data,
    #                                      partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     cargo = self.get_object()
    #     self.perform_destroy(cargo)
    #     return Response(status=status.HTTP_204_NO_CONTENT)