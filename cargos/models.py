from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    RegexValidator)
from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                         related_name='pick_up_location')
    delivery_location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                          related_name='delivery_location')
    weight = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)])
    description = models.TextField()


class Car(models.Model):
    number = models.CharField(max_length=5, unique=True, validators=[
        RegexValidator(regex=r"^.*$",
                       message="Допускаются только буквы и цифры")])
    current_location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                         related_name="cars")
    load_capacity = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)])
