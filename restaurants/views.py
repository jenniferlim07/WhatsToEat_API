from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def restaurant_list(request):
    # GET list of restaurants
    # or find by city
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()

        city = request.GET.get('city', None)
        if city is not None:
            restaurants = restaurants.filter(city__icontains=city)

        restaurants_serializer = RestaurantSerializer(restaurants, many=True)
        return JsonResponse(restaurants_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    # POST a new restaurant
    elif request.method == 'POST':
        restaurant_data = JSONParser().parse(request)
        restaurants_serializer = RestaurantSerializer(data=restaurant_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse(restaurants_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(restaurants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE all restaurants??
    elif request.method == 'DELETE':
        count = Restaurant.objects.all().delete()
        return JsonResponse({'message': '{} Restaurants were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def restaurant_detail(request, pk):
    # find restaurant by pk (id)
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return JsonResponse({'message': 'The restaurant does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET restaurant
    if request.method == 'GET':
        restaurants_serializer = RestaurantSerializer(restaurant)
        return JsonResponse(restaurants_serializer.data)

    # PUT / Update restaurant
    elif request.method == 'PUT':
        restaurant_data = JSONParser().parse(request)
        restaurants_serializer = RestaurantSerializer(restaurant, data=restaurant_data)
        if restaurants_serializer.is_valid():
            restaurants_serializer.save()
            return JsonResponse(restaurants_serializer.data)
        return JsonResponse(restaurants_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE restaurant
    elif request.method == 'DELETE':
        restaurant.delete()
        return JsonResponse({'message': 'Restaurant was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def restaurant_cities(request):
    # restaurants = Restaurant.objects.all()
    cities = Restaurant.objects.all().values('city')
    # cities = Restaurant.objects.values_list('city', flat=True).order_by('city').distinct()

    set_cities = []
    for city in cities:
        if city not in set_cities:
            set_cities.append(city)

    print("*** city", set_cities)
    restaurants_serializer = RestaurantSerializer(set_cities, many=True)
    return JsonResponse(restaurants_serializer.data, safe=False)


