from django.forms import ModelForm
from .models import Restaurant, RestaurantImages
from django import forms


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"

class RestaurantImagesForm(ModelForm):
    class Meta:
        widgets = {
        'image': forms.ClearableFileInput(attrs={'class': 'file-upload-input', 'id': 'file-selector',"multiple": True})
        }
        model = RestaurantImages
        fields =  "__all__"
