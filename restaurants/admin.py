from django.contrib import admin
from .models import Restaurant, Cuisine

class RestaurantAdmin(admin.ModelAdmin):
    list = ('id','name', 'website', 'address', 'city')

admin.site.register(Restaurant, RestaurantAdmin)

admin.site.register(Cuisine)

# Register your models here.
# from django.contrib import admin
# from . import models


# @admin.register(models.Restaurant)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id','name', 'website', 'address', 'city')


# admin.site.register(models.Restaurant)