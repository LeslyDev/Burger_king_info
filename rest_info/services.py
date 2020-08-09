import math
from rest_info.models import RestaurantKFC


def get_count_competitors(latitude, longitude):
    dist = 2
    upd_latitude = float(latitude)
    upd_longitude = float(longitude)
    lon1 = upd_longitude - dist / abs(math.cos(math.radians(upd_latitude)) * 111.0)
    lon2 = upd_longitude + dist / abs(math.cos(math.radians(upd_latitude)) * 111.0)
    lat1 = upd_latitude - (dist / 111.0)
    lat2 = upd_latitude + (dist / 111.0)
    count = RestaurantKFC.objects.filter(latitude__range=(lat1, lat2)).filter(longitude__range=(lon1, lon2)).count()
    return count
