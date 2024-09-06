from django.test import TestCase
from django.urls import reverse

class ApiTest(TestCase):

    def test_candlestick_data(self):
        response = self.client.get(reverse('candlestick-data'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json())

    def test_line_chart_data(self):
        response = self.client.get(reverse('line-chart-data'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('labels', response.json())
        self.assertIn('data', response.json())

    def test_bar_chart_data(self):
        response = self.client.get(reverse('bar-chart-data'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('labels', response.json())
        self.assertIn('data', response.json())

    def test_pie_chart_data(self):
        response = self.client.get(reverse('pie-chart-data'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('labels', response.json())
        self.assertIn('data', response.json())
