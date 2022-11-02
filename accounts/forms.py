from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from accounts.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('fullname','address' ,'username','email',)
        # fields = '__all__'