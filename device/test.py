
# Create your tests here.
from django.test import TestCase
from .models import Device

class DeviceModelTest(TestCase):
    def test_device_creation(self):
        device = Device.objects.create(name='Test Device')

        self.assertEqual(device.name, 'Test Device')

        self.assertIsNotNone(device.serial_number)

    def test_device_string_representation(self):
        device = Device.objects.create(name='Test Device')

        expected_result = 'Test Device'
        self.assertEqual(str(device), expected_result)