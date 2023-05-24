from django.contrib import admin

from .models import Car, Cargo, Location


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "current_location",
        "load_capacity",
    )


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "pick_up_location",
        "delivery_location",
        "weight",
        "description",
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "state",
        "zip_code",
        "latitude",
        "longitude",
    )
