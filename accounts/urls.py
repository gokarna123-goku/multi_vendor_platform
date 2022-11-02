from django import views
from django.urls import path
from accounts import views


app_name = 'accounts'


urlpatterns = [
    path('siginup/', views.RegisterView.as_view(), name='signup'),
    path("logout/",views.UserLogoutView.as_view(),name='logout'), 
    # path('siginin/', views.signin, name='signin'),
]
