from urllib import response
from django.test import TestCase, Client

# Create your tests here.

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register(self):
        response = self.client.get("/register/")

        self.assertEqual(response.status_code, 200)
    
    def test_login(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)
    
    def test_index(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
