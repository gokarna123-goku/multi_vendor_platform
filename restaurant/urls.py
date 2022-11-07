from django import views
from django.urls import path
from restaurant import views


app_name = 'homepage'


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('restaurant/', views.RestaurantView.as_view(), name='restaurant'),
    path('restaurant-detail/<str:restaurant_id>/', views.RestaurantDetailView.as_view(), name='restaurant-detail-data'),
    path('food/', views.FoodView.as_view(), name='food'),
    path('food-detail/<str:food_id>/', views.FoodDetailView.as_view(), name='food-detail'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog-detail/<str:blog_id>/<slug:blog_slug>/', views.BlogDetailView.as_view(), name='blog-detail-data'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('vendor/', views.vendorMembership, name='vendor'),
    path('add-to-cart-<str:fd_id>/', views.AddToCartView.as_view(), name="addtocart"),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('manage-cart/<int:cartfood_id>/', views.ManageView.as_view(), name='managecart'),
    path('empty-cart/', views.EmptyCartView.as_view(), name='emptycart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('payment/options/', views.payment, name='payment'),

    path('search/', views.SearchView.as_view(), name='search'),
]
