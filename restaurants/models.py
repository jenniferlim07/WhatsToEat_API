from django.db import models

# Create your models here.
class Restaurants(models.Model):
    # title = models.CharField(max_length=70, blank=False, default='')
    # description = models.CharField(max_length=200,blank=False, default='')
    # published = models.BooleanField(default=False)
    name = models.CharField(max_length=50, blank=False, default='')
    website = models.URLField(max_length=200, blank=True, default='')
    address = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=True)
    # state = USState
    zip_code = models.CharField(max_length=5, blank=True)