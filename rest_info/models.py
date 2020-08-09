from django.db import models


class RestaurantKFC(models.Model):
    some_id = models.SlugField(unique=True)
    latitude = models.DecimalField(decimal_places=15, max_digits=17)
    longitude = models.DecimalField(decimal_places=15, max_digits=17)

    def __str__(self):
        return self.some_id


class RestaurantBK(models.Model):
    some_id = models.SlugField(unique=True)
    latitude = models.DecimalField(decimal_places=15, max_digits=17)
    longitude = models.DecimalField(decimal_places=15, max_digits=17)
    address = models.CharField(max_length=255)
    competitors_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.some_id
