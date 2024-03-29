from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register([
    FoodCategory, 
    Food, 
    Cart, 
    CartFood, 
    Restaurant, 
    RestaurantCategory, 
    RestaurantAttribute, 
    RestaurantReview,
    Order, 
    Blog, 
    BlogReview, 
    Contact
    ])

# Ended