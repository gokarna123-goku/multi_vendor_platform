from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from accounts.models import User
from restaurant.models import Customer, Address
from django import forms 


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username',)
        # exclude = ('password',)
        # fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('fullname',)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('permanent_address', 'temporary_address', 'working_address',)

