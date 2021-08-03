from django.conf.urls import url
from restaurants import views
from django.urls import path

urlpatterns = [
    # url(r'^restaurants$', views.restaurant_list),
    # url(r'^restaurants/(?P<pk>[0-9]+)$', views.restaurant_detail)
    path('restaurants', views.restaurant_list),
    path('restaurants/<int:pk>', views.restaurant_list),
    path('restaurants/city', views.restaurant_cities)

]