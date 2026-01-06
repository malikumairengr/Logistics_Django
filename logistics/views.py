from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import models, serializers


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'capacity']
    search_fields = ['name', 'address']
    ordering_fields = ['name', 'capacity']
    ordering = ['name']


class DriverViewSet(viewsets.ModelViewSet):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'phone']
    ordering_fields = ['first_name', 'last_name']
    ordering = ['first_name']


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['model', 'capacity', 'driver']
    search_fields = ['license_plate', 'model']
    ordering_fields = ['license_plate', 'model', 'capacity']
    ordering = ['license_plate']


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = models.Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'origin', 'destination', 'vehicle', 'driver', 'weight']
    search_fields = ['reference']
    ordering_fields = ['created_at', 'updated_at', 'weight', 'status']
    ordering = ['-created_at']
