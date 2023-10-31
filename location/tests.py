from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Location
from api.serializers import LocationSerializer

class LocationAPITest(APITestCase):
    def setUp(self):
        self.location = Location.objects.create(
            region_name='Test Region',
            installation_date='2023-09-08' 
        )

    def test_retrieve_location(self):
        url = reverse('location-detail', args=[self.location.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer = LocationSerializer(self.location)
        expected_data = {
            'id': str(self.location.id),
            'region_name': 'Test Region',
            'updated_at': serializer.data['updated_at']
        }

    
