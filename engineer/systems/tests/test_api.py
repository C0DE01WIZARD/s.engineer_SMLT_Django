from rest_framework.test import APITestCase
from django.urls import reverse

class SystemsApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('api/v1/equipments_list')
        print(url)
        response = self.client.get(url)
        print(response)