from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Restaurants Home</h1>')

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def restaurant_list(request):
    # GET list of restaurants
    # or find by city
    if request.method == 'GET':
        # restaurants = Restaurant.objects.all()
        # print("response ", request)
        # Project.objects.filter(owner_id=currentUser).order_by('id')
        restaurants = Restaurant.objects.filter(user=request.user)
        # print("*** restaurants by user ", restaurants)
        # res_filter = restaurants.filter(city__icontains=city)

        city = request.GET.get('city', None)

        if city is not None:
            restaurants = restaurants.filter(city__icontains=city)
            print("filter ", restaurants)

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
    # elif request.method == 'DELETE':
    #     count = Restaurant.objects.all().delete()
    #     return JsonResponse({'message': '{} Restaurants were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


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

    # cities = Restaurant.objects.values('city').order_by('city').distinct()
    cities = Restaurant.objects.order_by('city').distinct('city').filter(user=request.user)

    # user_cities = cities.filter(user=request.user)
    # restaurants = Restaurant.objects.filter(user=request.user)
    # user_cities = restaurants.values('city').order_by('city').distinct()
    print(" user_cities ", cities)

    # print("*** city", set_cities)
    restaurants_serializer = RestaurantSerializer(cities, many=True)
    return JsonResponse(restaurants_serializer.data, safe=False)


# @api_view(['GET', 'POST'])
# def cuisine_list(request):
#     if request.method == 'GET':
#         cuisines = Cuisine.objects.values('types').order_by('types').distinct()
#         cuisine_serializer = CuisineSerializer(cuisines, many=True)
#         return JsonResponse(cuisine_serializer.data, safe=False)

#     elif request.method == 'POST':

#         cuisine_data = JSONParser().parse(request)
#         print("*** ", cuisine_data)
#         cuisine_serializer = CuisineSerializer(data=cuisine_data)
#         print("*** ", cuisine_serializer)
#         if cuisine_serializer.is_valid():
#             cuisine_serializer.save()
#             return JsonResponse(cuisine_serializer.data, status=status.HTTP_201_CREATED)
#         print("*** ", cuisine_serializer.errors)
#         return JsonResponse(cuisine_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


