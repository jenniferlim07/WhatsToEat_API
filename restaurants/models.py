from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    website = models.URLField(max_length=200, blank=True, default='')
    address = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=True)
    # state = USState
    zip_code = models.CharField(max_length=5, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)