from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'homepage/index.html')

def restaurant(request):
    return render(request, 'restaurant/restaurant.html')

def restoDetail(request):
    return render(request, 'restaurant/resto_detail.html')

def food(request):
    return render(request, 'foods/food.html')

def foodDetail(request):
    return render(request, 'foods/detail.html')

def blog(request):
    return render(request, 'blogs/blog.html')

def blogDetail(request):
    return render(request, 'blogs/blog_detail.html')

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
