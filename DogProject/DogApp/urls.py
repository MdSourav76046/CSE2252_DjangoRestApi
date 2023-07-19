from django.contrib import admin
from django.urls import path
from .views import DogShopList, DogShopDetail
urlpatterns = [
    path('dogshops/', DogShopList.as_view(), name="dog_shop_list"),
    path('dogshops/<int:pk>', DogShopDetail.as_view(), name="dog_shop_details")
]
