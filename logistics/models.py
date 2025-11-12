from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=30, unique=True)
    model = models.CharField(max_length=100, blank=True)
    capacity = models.IntegerField(default=0)
    driver = models.ForeignKey(Driver, null=True, blank=True, on_delete=models.SET_NULL, related_name='vehicles')

    def __str__(self):
        return self.license_plate


class Shipment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    reference = models.CharField(max_length=100, unique=True)
    origin = models.ForeignKey(Warehouse, related_name='outgoing_shipments', on_delete=models.PROTECT)
    destination = models.ForeignKey(Warehouse, related_name='incoming_shipments', on_delete=models.PROTECT)
    vehicle = models.ForeignKey(Vehicle, null=True, blank=True, on_delete=models.SET_NULL)
    driver = models.ForeignKey(Driver, null=True, blank=True, on_delete=models.SET_NULL)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reference
