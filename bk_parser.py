from geopy.geocoders import Nominatim
import requests
import re

geolocator = Nominatim(user_agent='find_city')
pattern_for_moscow = re.compile(r'Москва')
rest_bk = requests.get(
    'https://burgerking.ru/restaurant-locations-json-reply-new/')
counter = 1
with open('bk_rest.txt', 'w') as bk_rest:
    for i in rest_bk.json():
        latitude = i['latitude']
        longitude = i['longitude']
        location = geolocator.reverse("{}, {}".format(latitude, longitude))
        address = location.address
        full_address = address.split(',')
        short_address = full_address[0] + ',' + full_address[1] + ',' + full_address[2]
        moscow = pattern_for_moscow.search(address)
        if moscow:
            bk_rest.write('{"pk": %s, "model": "rest_info.restaurantbk", ' \
                          '"fields": {"some_id": %s, "latitude": %s, ' \
                          '"longitude":' \
                          ' %s, "address": "%s"}}, \n' % (
                              counter, i['storeId'],
                              latitude, longitude,
                              short_address))
