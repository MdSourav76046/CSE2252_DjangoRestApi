from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import DogShopSerializer

class post_dogShop_test(APITestCase):
    def setUp(self):
        self.dogShop_url = reverse('dog_shop_list')
        self.dogShop_data = {
            "name": "Test Cat",
            "price": 2000.00,
            "breed": "american whiskey",
            "description": "Test Discription",
        }
        return super().setUp()

    def test_can_create_dogshop(self):
        response = self.client.post(self.dogShop_url, self.dogShop_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class get_dogShop_list(APITestCase):
    def setUp(self):
        self.dogShop_url = reverse('dog_shop_list')
        return super().setUp()

    def test_can_get_dogshop(self):
        response = self.client.get(self.dogShop_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class get_dogShop_detail(APITestCase):
    def setUp(self):
        self.dogShop_data = {
            "name": "Test Dog",
            "price": 1000.00,
            "breed": "Indian dog",
            "description": "Highly ricky",
        }
        self.response = self.client.post(reverse('dog_shop_list'), self.dogShop_data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.dogShop_url = reverse('dog_shop_details', kwargs={'pk': 1})
        return super().setUp()

    def test_can_get_dogShop(self):
        response = self.client.get(self.dogShop_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #4b1eab390cc3319dbc2581101efb4087f15f057e
        #71e799ffef85f1639b507089b1b23b646fdb1aeb

class put_dogShop_test(APITestCase):
    def setUp(self):
        self.dogShop_data = {
            "name": "Test Cat",
            "price": 1000.00,
            "breed": "Indian dog",
            "description": "Test Discription",
        }
        self.response = self.client.post(reverse('dog_shop_list'), self.dogShop_data)
        print(self.response.data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.dogShop_url = reverse('dog_shop_details', kwargs={'pk': 1})
        return super().setUp()

    def test_can_put_dogShop(self):
        self.dogShop_data = {
            "name": "Test Cat2",
            "price": 1000.00,
            "breed": "Indian dog",
            "description": "Test Discription2",
        }
        response = self.client.put(self.dogShop_url, self.dogShop_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class delete_dogShop(APITestCase):
    def setUp(self):
        self.dogShop_data = {
            "name": "Test Cat",
            "price": 1000.00,
            "breed": "Indian dog",
            "description": "Test Discription",
        }
        self.response = self.client.post(reverse('dog_shop_list'), self.dogShop_data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.dogShop_url = reverse('dog_shop_details', kwargs={'pk': 1})
        return super().setUp()

    def test_can_delete_dogShop(self):
        response = self.client.delete(self.dogShop_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)