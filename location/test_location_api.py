from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from location.models import Location

class LocationAPITest(APITestCase):
    def create_location(self):
        # Create a location object for testing
        return Location.objects.create(region_name='Test Region')

    def test_update_location(self):
        location = self.create_location()
        url = reverse('location-detail', args=[location.id])
        updated_data = {'region_name': 'Updated Region'}
        response = self.client.put(url, data=updated_data, format='json')
        location.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(location.region_name, 'Updated Region')