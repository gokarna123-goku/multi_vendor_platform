from django import views
from django.urls import path
from restaurant import views


app_name = 'homepage'


urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('restaurant-detail/', views.restoDetail, name='restaurant-detail'),
    path('food/', views.food, name='food'),
    path('food-detail/', views.foodDetail, name='food-detail'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/options/', views.payment, name='payment'),
]
