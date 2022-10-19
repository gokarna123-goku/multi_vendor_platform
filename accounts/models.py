from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True,)
    email = models.EmailField(verbose_name='email address', max_length=255,)
    email_confirmed = models.BooleanField(default=False) #initially this field is false but will se chan
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False)
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


class Register(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=80, unique=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
