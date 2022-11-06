import datetime
import os
from django.db import models
import uuid
from django.conf import settings
from accounts.models import User

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


def get_file_path_for_food(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('foods/', filename)

class FoodCategory(models.Model):
    food_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food_category_title = models.CharField(max_length=150)

    def __str__(self):
        return self.food_category_title



# From the official models.py
class RestaurantCategory(models.Model):
    restaurant_category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.restaurant_category_name


def get_file_path_for_restaurant(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('restaurants/', filename)


class Restaurant(models.Model):
    restaurant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    restaurant_name = models.CharField(max_length=150, null=True, blank=True)
    restaurant_address = models.CharField(max_length=255, null=True, blank=True)
    restaurant_city = models.CharField(max_length=255, null=True, blank=True)
    restaurant_state = models.CharField(max_length=255, null=True, blank=True)
    restaurant_type = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE)
    restaurant_location_latitude = models.DecimalField(max_digits=15,decimal_places=2)
    restaurant_location_longitude = models.DecimalField(max_digits=15,decimal_places=2)
    restaurant_is_open = models.BooleanField(default=False)
    restaurant_hours_of_operation = models.TextField()
    restaurant_opening_time = models.TimeField()
    restaurant_closing_time = models.TimeField()
    restaurant_image = models.ImageField(upload_to=get_file_path_for_restaurant)
    restaurant_description = models.TextField()

    def __str__(self):
        return self.restaurant_name


class RestaurantAttribute(models.Model):
    Restaurant_attribute_id = models.OneToOneField(Restaurant,on_delete=models.CASCADE, primary_key=True, unique=True)
    bike_parking = models.CharField(max_length=150)
    accept_credit_cards = models.BooleanField(default=False)
    garage_parking = models.BooleanField(default=False)
    street_parking = models.BooleanField(default=False)
    dog_allowed = models.BooleanField(default=False)
    price_range = models.CharField(max_length=25, choices=PRICE_RANGE)
    valet = models.BooleanField(default=False)


class Food(models.Model):
    food_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    food_name = models.CharField(max_length=80)
    food_description = models.TextField()
    food_quantity = models.IntegerField()
    food_selling_price = models.DecimalField(max_digits=15,decimal_places=2)
    food_discound_price = models.DecimalField(max_digits=15,decimal_places=2)
    food_image = models.ImageField(upload_to=get_file_path_for_food)
    status= models.CharField(max_length=25, choices=OrderStatus)
    is_featured = models.BooleanField(default=False)
    food_category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.food_name

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Cart: ' + str(self.id)


class CartFood(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return 'Cart: ' + str(self.cart.id) + 'CartFood: ' + str(self.id)


ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the Way", "On the Way"),
    ("Order Completed", "Order Completed"),
    ("Order Cancelled", "Order Cancelled"),
    ("Order Delivered", "Order Delivered"),
)

COUNTRY = (
    ('Nepal', 'Nepal'),
)

TOWN_CITY = (
    ('Pyuthan', 'Pyuthan'),
    ('kathmandu', 'kathmandu'),
    ('Lalitpur', 'Lalitpur'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Dhading', 'Dhading'),
    ('Kaski', 'Kaski'),
    ('Butwal', 'Butwal'),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_by = models.CharField(max_length=200)
    country = models.CharField(max_length=200, choices=COUNTRY)
    town_city = models.CharField(max_length=200, choices=TOWN_CITY)
    shipping_address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    subtotal = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Order: ' + str(self.order_by) 



def get_file_path_for_blog(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('blogs/', filename)

class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    blog_slug = models.SlugField(unique=True)
    blog_category_name = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=150, null=False, blank=False)
    blog_description = models.TextField()
    blog_publish_date = models.DateField(auto_now_add=True)
    blog_image = models.ImageField(upload_to=get_file_path_for_blog)

    def __str__(self):
        return self.blog_title


# Ended