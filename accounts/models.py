from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.contrib import messages
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
# from django.contrib.auth.views import login

# Create your models here.


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(verbose_name='email address', max_length=255)
    email_confirmed = models.BooleanField(default=False) #initially this field is false but will se chan
    is_active = models.BooleanField(default=True) # can login
    is_staff = models.BooleanField(default=False) # a staff user; non super-user
    is_admin = models.BooleanField(default=False) # superusr or admin
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #emaila nd password are required fields and first name and last name is inherited from the user creation model

    #instanciate the usermanager object
    object = UserManager()

    # def get_username(self):
    #     username = self.first_name+"."+self.last_name
    #     return username

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name


class ActivateAccount(generic.View):
     def get(self, request, uidb64, token, *args, **kwargs):
         try:
             # uid = force_bytes(urlsafe_base64_decode(uidb64)).decode()
             uid = force_bytes(urlsafe_base64_decode(uidb64))
             user = User.objects.get(id=uid)
             # print(uid)
         except (TypeError, ValueError, OverflowError, User.DoesNotExist):
             user = None
         # User = get_user_model()
         # print(uid)
         # uid = force_text(urlsafe_base64_decode(uidb64))#.decode()
         # # uid = int(uida,10) invalid literal for int() with base 10: b'l\xc4'
         # #the value of uid is b'l\xcc' need to convert this to 1
         # user = User.objects.get(id=uid)
         # # print(uid)

         if user is not None and default_token_generator.check_token(user, token):
             # obj, created = User.objects.get_or_create(user=user)
             user.is_active = True
             user.email_confirmed = True
             user.save()
            #  login(request, user)
             messages.success(request,('Your account have been confirmed.'))
             return redirect('accounts:profile')
         else:
             # messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
             # return redirect('accounts:activation_invalid')
             return HttpResponse ('The confirmation link was invalid, possibly because it has already been used.')

# def activation_sent_view(request):
#     return render(request,'registration/activation_sent.html')

# def activation_invalid_view(request):
#     return render(request,'registration/activation_invalid.html')

# class Register(models.Model):
#     fullname = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     username = models.CharField(max_length=80, unique=True)
#     password1 = models.CharField(max_length=50)
#     password2 = models.CharField(max_length=50)
