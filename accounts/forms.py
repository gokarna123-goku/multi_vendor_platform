from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from accounts.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username',)
        # exclude = ('password',)
        # fields = '__all__'