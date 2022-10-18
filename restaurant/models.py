import datetime
import os
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings

PRICE_RANGE = (
        ('Low Price','Low Price'),
        ('Medium Price','Medium Price'),
        ('Expensive','Expensive'),
    )

GENDERS = (
        ('m','male'),
        ('f','female'),
        ('o','other'),
    )

OrderStatus = (
        ('Order Processing','Order Processing'),
        ('Order Received','Order Received'),
        ('Order Preparing','Order Preparing'),
        ('Order On-Delivery','Order On-Delivery'),
        ('Order Delivered','Order Delivered'),
    )

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


# From the official models.py
class RestaurantCategory(models.Model):
    restaurant_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_category_name = models.CharField(max_length=150)
    def __str__(self):
        return self.restaurant_category_name


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('restaurants/', filename)

class RestaurantImages(models.Model):
    Restaurant_image_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=get_file_path)

    # def __str__(self):
    #     return self.Restaurant_image_id


class Restaurant(models.Model):
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    Restaurant_type = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=15,decimal_places=2)
    longitude = models.DecimalField(max_digits=15,decimal_places=2)
    is_open = models.BooleanField(default=False)
    hours_of_operation = models.TextField()
    restaurant_image = models.ForeignKey(RestaurantImages,on_delete=models.CASCADE)
    # images = models.ImageField(null=False, blank=False)

    def __str__(self):

        return self.name


class RestaurantAttribute(models.Model):
    Restaurant_attribute_id = models.OneToOneField(Restaurant,on_delete=models.CASCADE, primary_key=True, unique=True)
    bike_parking = models.CharField(max_length=150)
    accept_credit_cards = models.BooleanField(default=False)
    garage_parking = models.BooleanField(default=False)
    street_parking = models.BooleanField(default=False)
    dog_allowed = models.BooleanField(default=False)
    price_range = models.CharField(max_length=25, choices=PRICE_RANGE)
    valet = models.BooleanField(default=False)



class Menu(models.Model):
    menu_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    food = models.ForeignKey(Food,on_delete=models.CASCADE, null=True, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)



class FoodCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Food(models.Model):
    food_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    food_image = models.ImageField(upload_to="foods")
    food_price = models.PositiveIntegerField()
    discount_price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.food_name


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Cart: ' + str(self.id)



ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the Way", "On the Way"),
    ("Order Completed", "Order Completed"),
    ("Order Cancelled", "Order Cancelled"),
    ("Order Delivered", "Order Delivered"),
)

class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Order: ' + str(self.id) 





# Ended