import unittest
from app import app  # Adjust 'app' based on your Flask app filename

class WeatherAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_city(self):
        response = self.app.get('/weather?city=New+York')
        self.assertEqual(response.status_code, 200)
        self.assertIn('New York', response.get_data(as_text=True))

    def test_invalid_city(self):
        response = self.app.get('/weather?city=InvalidCity')
        self.assertEqual(response.status_code, 404)
        self.assertIn('City not found', response.get_data(as_text=True))

    def test_missing_city(self):
        response = self.app.get('/weather')
        self.assertEqual(response.status_code, 400)
        self.assertIn('City not provided', response.get_data(as_text=True))
