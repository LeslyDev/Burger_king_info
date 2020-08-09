from django.contrib import admin

from rest_info.models import RestaurantBK, RestaurantKFC


@admin.register(RestaurantBK)
class RestaurantBKAdmin(admin.ModelAdmin):
    pass


@admin.register(RestaurantKFC)
class RestaurantBKAdmin(admin.ModelAdmin):
    pass
