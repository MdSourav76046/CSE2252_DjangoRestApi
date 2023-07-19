from django.shortcuts import render
from rest_framework import generics
from .models import DogShop
from .serializers import DogShopSerializer


class DogList(generics.ListCreateAPIView):
    queryset = DogShop.objects.all()
    serializer_class = DogShopSerializer


class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DogShop.objects.all()
    serializer_class = DogShopSerializer

