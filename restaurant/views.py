from django.shortcuts import render
from django.views import generic
from .models import *


# Create your views here.

def home(request):
    return render(request, 'homepage/index.html')

class RestaurantView(generic.ListView):
    # model = Restaurant
    # context_object_name = 'restaurants_list'

    def get(self, request, *args, **kwargs):
        template_name = "restaurant/restaurant.html"
        restaurants_list = Restaurant.objects.all()
        print(restaurants_list)
        context = {
            'restaurants_list': restaurants_list
        }
        return render(request, template_name, context)

# def restaurant(request):
#     return render(request, 'restaurant/restaurant.html')

class RestaurantDetailView(generic.DetailView):

    def get(self, request, *args, **kwargs):
        template_name = "restaurant/resto_detail.html"
        restaurant_detail_list = Restaurant.objects.get(restaurant_id=self.kwargs.get('restaurant_id'))
        context = {
            'restaurant_detail_list': restaurant_detail_list,
        }
        return render(request, template_name, context)


def food(request):
    return render(request, 'foods/food.html')

def foodDetail(request):
    return render(request, 'foods/detail.html')

class BlogView(generic.ListView):
    def get(self, request, *args, **kwargs):
        template_name = 'blogs/blog.html'
        blogs_list = Blog.objects.all()
        context = {
            'blogs_list' : blogs_list,
        }
        return render(request, template_name, context)


class BlogDetailView(generic.ListView):
    def get(self, request, *args, **kwargs):
        template_name = 'blogs/blog_detail.html'
        blog_detail_list = Blog.objects.get(blog_id=self.kwargs.get('blog_id'), blog_slug=self.kwargs.get('blog_slug'))
        context = {
            'blog_detail_list' : blog_detail_list,
        }
        return render(request, template_name, context)

# def blogDetail(request):
#     return render(request, 'blogs/blog_detail.html')

def contact(request):
    return render(request, 'contact/contact.html')

def vendorMembership(request):
    return render(request, 'vendor/vendor.html')

def cart(request):
    return render(request, 'homepage/cart.html')

def checkout(request):
    return render(request, 'homepage/checkout.html')

def payment(request):
    return render(request, 'homepage/payment.html')

# 
