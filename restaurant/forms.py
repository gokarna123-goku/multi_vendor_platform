from django.forms import ModelForm
from .models import Order, Contact
from django import forms


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_by', 'country', 'town_city', 'shipping_address', 'postal_code', 'mobile', 'email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['fullname', 'email', 'message']

# class RestaurantForm(ModelForm):
#     class Meta:
#         model = Restaurant
#         fields = "__all__"

# class RestaurantImagesForm(ModelForm):
#     class Meta:
#         widgets = {
#         'image': forms.ClearableFileInput(attrs={'class': 'file-upload-input', 'id': 'file-selector',"multiple": True})
#         }
#         model = RestaurantImages
#         fields =  "__all__"
