from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    # model: the model for Serializer
    # fields: a tuple of field names to be included in the serialization
    class Meta:
        model = Restaurant
        fields = ('__all__')