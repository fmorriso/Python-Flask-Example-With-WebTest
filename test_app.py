from webtest import TestApp
import unittest
from app import app  # Import the Flask app

class FlaskWebTest(unittest.TestCase):
    def setUp(self):
        self.test_app = TestApp(app)  # Wrap Flask app with WebTest

    def test_home_page(self):
        response = self.test_app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the Flask App!", response.text)

    def test_json_route(self):
        response = self.test_app.get('/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], "Hello, WebTest!")

    def test_post_request(self):
        response = self.test_app.post_json('/echo', {'name': 'ChatGPT'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'name': 'ChatGPT'})

if __name__ == '__main__':
    unittest.main()
