from django.db import models

# Create your models here.
class DogShop(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    breed = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
