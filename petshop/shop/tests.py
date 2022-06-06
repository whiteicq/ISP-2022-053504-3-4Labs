from urllib import response
from django.test import TestCase, Client
from . import models

# Create your tests here.

class ViewTests(TestCase):
    def setUp(self):
        self.classification = models.Classification.objects.get_or_create(
            title="Testclass"
        )[0]
        self.classification.save()
        models.Animal.objects.get_or_create(
            title="Animal1",
            price='123',
            weight='55',
            seller_number='12456',
            classification=self.classification
        )[0].save()
        models.Animal.objects.get_or_create(
            title="Animal2",
            price='124',
            weight='51',
            seller_number='12456',
            classification=self.classification
        )[0].save()
        
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
    
    def test_classification(self):
        response = self.client.get(f"/classification/{self.classification.pk}/")
        
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['animals'], models.Animal.objects.filter(classification=self.classification))
    
    def test_classification_404(self):
        response = self.client.get("/classification/999/")
        
        self.assertEqual(response.status_code, 404)
        
    def test_animal(self):
        animal = models.Animal.objects.all()[0]
        response = self.client.get(f"/animal/{animal.pk}")
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['animal_item'], animal)

    def test_animal_301(self):
        response = self.client.get("/animal/999")
        
        self.assertEqual(response.status_code, 404)
