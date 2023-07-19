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


# class put_cat_test(APITestCase):
#     def setUp(self):
#         self.cat_data = {
#             "name": "Test Cat",
#             "price": 1000.00,
#             "description": "Test Discription",
#         }
#         self.response = self.client.post(reverse('product_view'), self.cat_data)
#         print(self.response.data)
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
#         self.cat_url = reverse('product_details', kwargs={'pk': 1})
#         return super().setUp()

#     def test_can_put_cat(self):
#         self.cat_data = {
#             "name": "Test Cat2",
#             "price": 1000.00,
#             "description": "Test Discription2",
#         }
#         response = self.client.put(self.cat_url, self.cat_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class delete_cat(APITestCase):
#     def setUp(self):
#         self.cat_data = {
#             "name": "Test Cat",
#             "price": 1000.00,
#             "description": "Test Discription",
#         }
#         self.response = self.client.post(reverse('product_view'), self.cat_data)
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
#         self.cat_url = reverse('product_details', kwargs={'pk': 1})
#         return super().setUp()

#     def test_can_delete_cat(self):
#         response = self.client.delete(self.cat_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)