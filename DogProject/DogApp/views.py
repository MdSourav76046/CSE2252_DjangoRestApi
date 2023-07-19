from django.shortcuts import render
from rest_framework import generics
from .models import DogShop
from .serializers import DogShopSerializer


class DogShopShopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DogShop.objects.all()
    serializer_class = DogShopSerializer

