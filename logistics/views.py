from rest_framework import viewsets
from . import models, serializers


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = models.Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer
