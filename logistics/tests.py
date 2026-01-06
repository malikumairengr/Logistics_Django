from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from logistics import models


class ModelsTest(TestCase):
    def test_create_warehouse(self):
        w = models.Warehouse.objects.create(name='Main', capacity=1000)
        self.assertEqual(str(w), 'Main')

    def test_shipment_reference_unique(self):
        w1 = models.Warehouse.objects.create(name='A')
        w2 = models.Warehouse.objects.create(name='B')
        s = models.Shipment.objects.create(reference='REF1', origin=w1, destination=w2)
        self.assertEqual(str(s), 'REF1')


class APITest(APITestCase):
    def setUp(self):
        # Create test data
        self.warehouse1 = models.Warehouse.objects.create(name='Warehouse A', capacity=1000)
        self.warehouse2 = models.Warehouse.objects.create(name='Warehouse B', capacity=2000)

        self.driver1 = models.Driver.objects.create(first_name='John', last_name='Doe')
        self.driver2 = models.Driver.objects.create(first_name='Jane', last_name='Smith')

        self.vehicle1 = models.Vehicle.objects.create(license_plate='ABC123', model='Truck', capacity=5000, driver=self.driver1)
        self.vehicle2 = models.Vehicle.objects.create(license_plate='XYZ789', model='Van', capacity=3000, driver=self.driver2)

        self.shipment1 = models.Shipment.objects.create(
            reference='SHIP001',
            origin=self.warehouse1,
            destination=self.warehouse2,
            vehicle=self.vehicle1,
            driver=self.driver1,
            weight=1000.50,
            status='pending'
        )
        self.shipment2 = models.Shipment.objects.create(
            reference='SHIP002',
            origin=self.warehouse2,
            destination=self.warehouse1,
            vehicle=self.vehicle2,
            driver=self.driver2,
            weight=500.25,
            status='in_transit'
        )

    def test_warehouse_filtering(self):
        # Test filtering by name
        response = self.client.get('/api/warehouses/?name=Warehouse A')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Warehouse A')

        # Test filtering by capacity
        response = self.client.get('/api/warehouses/?capacity=2000')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['capacity'], 2000)

    def test_warehouse_search(self):
        # Test search by name
        response = self.client.get('/api/warehouses/?search=Warehouse')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_warehouse_ordering(self):
        # Test ordering by name
        response = self.client.get('/api/warehouses/?ordering=name')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Warehouse A')
        self.assertEqual(response.data['results'][1]['name'], 'Warehouse B')

        # Test ordering by capacity descending
        response = self.client.get('/api/warehouses/?ordering=-capacity')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['capacity'], 2000)
        self.assertEqual(response.data['results'][1]['capacity'], 1000)

    def test_shipment_filtering(self):
        # Test filtering by status
        response = self.client.get('/api/shipments/?status=pending')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['status'], 'pending')

    def test_shipment_search(self):
        # Test search by reference
        response = self.client.get('/api/shipments/?search=SHIP001')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['reference'], 'SHIP001')

    def test_shipment_ordering(self):
        # Test ordering by weight
        response = self.client.get('/api/shipments/?ordering=weight')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['weight'], '500.25')
        self.assertEqual(response.data['results'][1]['weight'], '1000.50')

    def test_pagination(self):
        # Create more data for pagination test
        for i in range(15):
            models.Warehouse.objects.create(name=f'Warehouse {i}', capacity=100 * i)

        # Test pagination (PAGE_SIZE = 10)
        response = self.client.get('/api/warehouses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)  # Should be paginated
        self.assertIn('next', response.data)  # Should have pagination links
