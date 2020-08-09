from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from rest_info.models import RestaurantBK
from rest_info.services import get_count_competitors


def start_redirect(request):
    return redirect('list_of_restaurants/')


def list_of_restaurants(request):
    template = loader.get_template('list_of_restaurants.html')
    bk_restaurant = RestaurantBK.objects.all()
    for i in bk_restaurant:
        latitude = i.latitude
        longitude = i.longitude
        count = get_count_competitors(latitude, longitude)
        i.competitors_count = count
        i.save()
    bk_restaurant_ordered = bk_restaurant.order_by('-competitors_count')
    restaurants_list = {
        "restaurants_list": bk_restaurant_ordered
    }
    return HttpResponse(template.render(restaurants_list, request))

