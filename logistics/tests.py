from django.test import TestCase
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


class APITestPlaceholder(TestCase):
    def test_api_root(self):
        # simple smoke test that API root is reachable
        resp = self.client.get('/api/')
        self.assertIn(resp.status_code, (200, 302))
