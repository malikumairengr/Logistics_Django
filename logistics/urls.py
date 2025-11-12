from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'warehouses', views.WarehouseViewSet)
router.register(r'drivers', views.DriverViewSet)
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'shipments', views.ShipmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
