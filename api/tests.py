from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class CadastralPlotViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_existing_cadastral_plot(self):
        cadastral_number = '24:39:0101001:369'
        response = self.client.get(f'/v1/cadastral/{cadastral_number}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_non_existing_cadastral_plot(self):
        cadastral_number = '99999'
        response = self.client.get(f'/v1/cadastral/{cadastral_number}/').json()
        self.assertEqual(response['status'], 'Not found')

    def test_post_cadastral_plot(self):
        cadastral_number = '24:39:0101001:369'
        response = self.client.post(f'/v1/cadastral/{cadastral_number}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('cadastral_number', response.data)
        self.assertIn('short_cadastral_number', response.data)
        self.assertIn('geometry', response.data)
        self.assertIn('address', response.data)
