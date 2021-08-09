from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):

    # model: the model for Serializer
    # fields: a tuple of field names to be included in the serialization
    # cuisine = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'user', 'name', 'website', 'address', 'city')


# class CuisineSerializer(serializers.ModelSerializer):
#     restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all(), many=False)

#     class Meta:
#         model = Cuisine
#         fields = ('__all__')