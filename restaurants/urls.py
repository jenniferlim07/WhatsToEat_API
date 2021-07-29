from django.conf.urls import url
from restaurants import views

urlpatterns = [
    url(r'^restaurants$', views.restaurant_list),
    url(r'^restaurants/(?P<pk>[0-9]+)$', views.restaurant_detail)
]