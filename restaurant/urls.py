from django import views
from django.urls import path
from restaurant import views


app_name = 'homepage'


urlpatterns = [
    path('', views.home, name='home'),
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('restaurant-detail/<str:restaurant_id>/', views.RestaurantDetailView.as_view(), name='restaurant-detail-data'),
    path('food/', views.food, name='food'),
    path('food-detail/', views.foodDetail, name='food-detail'),
    path('blog/', views.blog, name='blog'),
    path('blog-detail/', views.blogDetail, name='blog-detail'),
    path('contact/', views.contact, name='contact'),
    path('vendor/', views.vendorMembership, name='vendor'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/options/', views.payment, name='payment'),
]
