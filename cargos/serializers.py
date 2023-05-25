from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from cargos.models import Car, Cargo, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["city", "state", "zip_code", "latitude", "longitude"]


class CargoSerializer(serializers.ModelSerializer):
    pick_up_location = LocationSerializer()
    delivery_location = LocationSerializer()

    class Meta:
        model = Cargo
        fields = ["id", "pick_up_location", "delivery_location", "weight",
                  "description"]


class CargoCreateSerializer(serializers.ModelSerializer):
    pick_up_location = serializers.CharField(max_length=5)
    delivery_location = serializers.CharField(max_length=5)

    def validate(self, data):
        pick_up_location = data.get('pick_up_location')
        delivery_location = data.get('delivery_location')

        if pick_up_location and delivery_location:
            pick_up_location_obj = get_object_or_404(Location,
                                                     zip_code=pick_up_location)
            delivery_location_obj = get_object_or_404(Location,
                                                      zip_code=delivery_location)

            data['pick_up_location'] = pick_up_location_obj
            data['delivery_location'] = delivery_location_obj

        return data

    class Meta:
        model = Cargo
        fields = ['pick_up_location', 'delivery_location', 'weight',
                  'description']


class CargoUpdateSerializer(serializers.Serializer):
    weight = serializers.IntegerField(min_value=1, max_value=1000)
    description = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        instance.weight = validated_data.get('weight', instance.weight)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.save()
        return instance
