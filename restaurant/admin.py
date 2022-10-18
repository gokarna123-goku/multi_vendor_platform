from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register([Customer, FoodCategory, Food, Cart, Order, Restaurant, RestaurantCategory, RestaurantImages, RestaurantAttribute, Menu])

# Ended