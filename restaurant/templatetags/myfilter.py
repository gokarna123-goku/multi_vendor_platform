from django import template
from restaurant.models import Restaurant, FoodCategory, Food

register = template.Library()

@register.filter(name='foodfilter')
def foodfilter(value, arg):
    foods = Food.objects.filter(restaurant=value, food_category=arg)
    return foods
