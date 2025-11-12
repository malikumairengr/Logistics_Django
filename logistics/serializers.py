from rest_framework import serializers
from . import models


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shipment
        fields = '__all__'
