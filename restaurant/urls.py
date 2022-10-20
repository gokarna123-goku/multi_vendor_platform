from django import views
from django.urls import path
from restaurant import views


app_name = 'homepage'


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('restaurant-detail/<str:restaurant_id>/', views.RestaurantDetailView.as_view(), name='restaurant-detail-data'),
    path('food/', views.food, name='food'),
    path('food-detail/', views.foodDetail, name='food-detail'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog-detail/<str:blog_id>/<slug:blog_slug>/', views.BlogDetailView.as_view(), name='blog-detail-data'),
    path('contact/', views.contact, name='contact'),
    path('vendor/', views.vendorMembership, name='vendor'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/options/', views.payment, name='payment'),
]
