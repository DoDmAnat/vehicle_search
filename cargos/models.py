from django.core.validators import (MinValueValidator, MaxValueValidator,
                                    RegexValidator)
from django.db import models


class Location(models.Model):
    city = models.CharField("Город", max_length=100)
    state = models.CharField("Штат", max_length=100)
    zip_code = models.CharField("Почтовый индекс(zip)", max_length=100)
    latitude = models.FloatField("Ширина")
    longitude = models.FloatField("Долгота")

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.zip_code


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location,
                                         verbose_name="Точка загрузки",
                                         on_delete=models.CASCADE,
                                         related_name='pick_up_location')
    delivery_location = models.ForeignKey(Location,
                                          verbose_name="Точка доставки",
                                          on_delete=models.CASCADE,
                                          related_name='delivery_location')
    weight = models.IntegerField("Вес груза",
                                 validators=[MinValueValidator(1),
                                             MaxValueValidator(1000)])
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Груз"
        verbose_name_plural = "Грузы"


class Car(models.Model):
    number = models.CharField("Номер машины", max_length=5, unique=True,
                              validators=[
                                  RegexValidator(regex=r"^[1-9]\d{3}[A-Z]$",
                                                 message="Номер в формате 1111A, 9999Z")])
    current_location = models.ForeignKey(Location,
                                         verbose_name="Локация машины",
                                         on_delete=models.CASCADE,
                                         related_name="cars")
    load_capacity = models.IntegerField("Грузоподъемность",
                                        validators=[MinValueValidator(1),
                                                    MaxValueValidator(1000)])

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return self.number
