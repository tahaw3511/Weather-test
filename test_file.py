import unittest
from app import app

class WeatherAPITestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client using the Flask application
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_city(self):
        # Test for a valid city: New York
        response = self.app.get('/weather?city=New+York')
        self.assertEqual(response.status_code, 200)
        self.assertIn('New York', response.get_data(as_text=True))
        self.assertIn('Cloudy', response.get_data(as_text=True))

    def test_invalid_city(self):
        # Test for a city that is not in the data: Tokyo
        response = self.app.get('/weather?city=Tokyo')
        self.assertEqual(response.status_code, 404)
        self.assertIn('City not found', response.get_data(as_text=True))

    def test_missing_city(self):
        # Test for when no city is provided in the request
        response = self.app.get('/weather')
        self.assertEqual(response.status_code, 400)
        self.assertIn('City not provided', response.get_data(as_text=True))

    def test_another_valid_city(self):
        # Test for another valid city: Los Angeles
        response = self.app.get('/weather?city=Los+Angeles')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sunny', response.get_data(as_text=True))

if _name_ == '_main_':
    unittest.main()
