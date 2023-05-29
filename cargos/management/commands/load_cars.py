import string

from django.core.management.base import BaseCommand

from cargos.models import Car, Location
from django.db.models import Count
import random


class Command(BaseCommand):
    help = 'Заполнения БД машинами'

    @staticmethod
    def generate_random_numbers():
        unique_numbers = set()

        while len(unique_numbers) < 20:
            number = (f"{random.randint(1000, 9999)}"
                      f"{random.choice(string.ascii_uppercase)}")
            unique_numbers.add(number)

        return list(unique_numbers)

    def handle(self, *args, **options):
        locations_count = Location.objects.aggregate(
            total=Count('id')
        )['total']

        random_numbers = self.generate_random_numbers()
        for i in range(20):
            random_index = random.randint(0, locations_count - 1)
            random_location = Location.objects.get(id=random_index)
            car = Car(
                number=random_numbers[i],
                current_location=random_location,
                load_capacity=random.randint(1, 1000),
            )
            print(car.current_location)
            car.save()