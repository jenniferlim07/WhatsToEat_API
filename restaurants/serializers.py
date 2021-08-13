from rest_framework import serializers
from restaurants.models import Restaurant, Cuisine


class CuisineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cuisine
        fields = ('id', 'type')

class RestaurantSerializer(serializers.ModelSerializer):

    # model: the model for Serializer
    # fields: a tuple of field names to be included in the serialization
    # cuisine = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    cuisine = CuisineSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'user', 'name', 'website', 'address', 'city', 'cuisine',)


