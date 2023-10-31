from django.test import TestCase
from device.models import Device
from .models import TemperatureHumidityRecord

class TemperatureHumidityRecordModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.device = Device.objects.create(name='Test Device')

    def test_humidity_with_unit(self):
        record = TemperatureHumidityRecord.objects.create(
            device=self.device,
            humidity=60.25,
            temperature=25.50
        )

        expected_result = '60.25% RH'
        self.assertEqual(record.humidity_with_unit, expected_result)

    def test_temperature_with_unit(self):
        record = TemperatureHumidityRecord.objects.create(
            device=self.device,
            humidity=60.25,
            temperature=25.5
        )

        expected_result = '25.5°C'
        self.assertEqual(record.temperature_with_unit, expected_result)