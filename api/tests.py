from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class BankDetailsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_home(self):
        url = reverse('api_home')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
