from django.http import Http404
from django.urls import reverse
from httplib2 import Response
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase
from location.models import Location
from api.serializers import LocationSerializer
from temperature_recording.models import TemperatureHumidityRecord

from rest_framework.test import APITestCase
from rest_framework import status
from flowrate.models import Device, FlowRate
from api.serializers import DeviceSerializer, FlowRateSerializer,TemperatureHumidityRecordSerializer

class LocationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def create_location(self, region_name="Test Region", installation_date="2023-09-08"):
        return Location.objects.create(region_name=region_name, installation_date=installation_date)

    def test_create_location(self):
        url = reverse('location-list-create')
        data = {
            'region_name': 'New Test Region',
            'installation_date': '2023-09-09'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 1)
        self.assertEqual(Location.objects.get().region_name, 'New Test Region')

    def test_list_locations(self):
        self.create_location()
        url = reverse('location-list-create')
        response = self.client.get(url)
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_location(self):
        location = self.create_location()
        url = reverse('location-detail', args=[location.id])
        response = self.client.get(url)
        serializer = LocationSerializer(location)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_location(self):
      location = self.create_location()
      url = reverse('location-detail', args=[location.id])
      updated_data = {'region_name': 'Updated Region'}
      response = self.client.put(url, updated_data, format='json')
      location.refresh_from_db()
   

    def test_delete_location(self):
        location = self.create_location()
        url = reverse('location-detail', args=[location.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Location.objects.count(), 0)

class DeviceAPITestCase(APITestCase):
    def test_device_list_api(self):
        device1 = Device.objects.create(device_owner="Rose Kivuva")
        device2 = Device.objects.create(device_owner="Ann Aketch")

        response = self.client.get(reverse('device-list'))

        serializer = DeviceSerializer([device1, device2], many=True)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_device_detail_api(self):
        device = Device.objects.create(device_owner="Test Device")

        response = self.client.get(reverse('device-detail', args=[device.pk]))

        serializer = DeviceSerializer(device)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_device_create_api(self):
        data = {'device_owner': 'New Device Owner'}

        response = self.client.post(reverse('device-list'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Device.objects.count(), 1)
        self.assertEqual(Device.objects.get().device_owner, 'New Device Owner')

    def test_device_update_api(self):
        device = Device.objects.create(device_owner="Old Owner")
        data = {'device_owner': 'New Owner'}

        response = self.client.put(reverse('device-detail', args=[device.pk]), data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Device.objects.get().device_owner, 'New Owner')

    def test_device_delete_api(self):
        device = Device.objects.create(device_owner="To be deleted")

        response = self.client.delete(reverse('device-detail', args=[device.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Device.objects.count(), 0)


class FlowRateAPITestCase(APITestCase):
    def test_flowrate_list_api(self):
        device1 = Device.objects.create(device_owner="Ann Aketch")
        device2 = Device.objects.create(device_owner="Rose Kivuva")

        flow1 = FlowRate.objects.create(device=device1, flow_rate=0.0014)
        flow2 = FlowRate.objects.create(device=device2, flow_rate=0.0136)

        response = self.client.get(reverse('flowrate-list'))

        serializer = FlowRateSerializer([flow1, flow2], many=True)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_flowrate_detail_api(self):
        device = Device.objects.create(device_owner="Test Device")
        flow = FlowRate.objects.create(device=device, flow_rate=0.2542)

        response = self.client.get(reverse('flowrate-detail', args=[flow.pk]))

        serializer = FlowRateSerializer(flow)
        expected_data = serializer.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_flowrate_create_api(self):
        device = Device.objects.create(device_owner="Test Device")
        data = {'device': device.pk, 'flow_rate': 0.1234}

        response = self.client.post(reverse('flowrate-list'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FlowRate.objects.count(), 1)
        self.assertEqual(FlowRate.objects.get().flow_rate, 0.1234)

    def test_flowrate_update_api(self):
        device = Device.objects.create(device_owner="Test Device")
        flow = FlowRate.objects.create(device=device, flow_rate=0.1234)
        data = {'device': device.pk, 'flow_rate': 0.5678}

        response = self.client.put(reverse('flowrate-detail', args=[flow.pk]), data)


    def test_flowrate_delete_api(self):
        device = Device.objects.create(device_owner="Test Device")
        flow = FlowRate.objects.create(device=device, flow_rate=0.1234)

        response = self.client.delete(reverse('flowrate-detail', args=[flow.pk]))



class TemperatureHumidityRecordSerializerTest(APITestCase):
    def setUp(self):
        self.device = Device.objects.create(name='Test Device')

        self.record = TemperatureHumidityRecord.objects.create(
            device=self.device,
            humidity=60.25,
            temperature=25.50
        )

        self.serializer = TemperatureHumidityRecordSerializer(instance=self.record)

    def test_serializer_fields(self):
        expected_fields = ['id', 'device', 'time_stamp', 'humidity_with_unit', 'temperature_with_unit']
        self.assertEqual(list(self.serializer.fields.keys()), expected_fields)

    def test_humidity_with_unit(self):
        expected_result = '60.25% RH'
        self.assertEqual(self.serializer.data['humidity_with_unit'], expected_result)

    def test_temperature_with_unit(self):
        expected_result = '25.5°C'
        self.assertEqual(self.serializer.data['temperature_with_unit'], expected_result)