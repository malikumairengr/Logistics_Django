from django.contrib import admin
from . import models


@admin.register(models.Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')


@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'model', 'capacity', 'driver')


@admin.register(models.Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('reference', 'origin', 'destination', 'status', 'created_at')
    list_filter = ('status',)
