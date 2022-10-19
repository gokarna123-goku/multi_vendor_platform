from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from accounts.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # fields = {'fullname', 'email', 'address', 'phone', 'username', 'password1', 'password2'}
        fields = '__all__'