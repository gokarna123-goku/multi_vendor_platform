from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register([Customer, FoodCategory, Food, Restaurant, RestaurantCategory, RestaurantAttribute, Menu, Blog])

# Ended