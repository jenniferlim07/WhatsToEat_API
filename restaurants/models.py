from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Cuisine(models.Model):
    type = models.CharField(max_length=70, blank=False, default='')
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type


class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    website = models.URLField(max_length=200, blank=True, default='')
    address = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=True)
    # state = USState
    zip_code = models.CharField(max_length=5, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    cuisine = models.ManyToManyField(Cuisine, related_name="restaurants")

    def __str__(self):
        return self.name
