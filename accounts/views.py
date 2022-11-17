from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import RegisterForm, CustomerForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


# Create your views here.

class RegisterView(generic.View):
    # form_class = RegisterForm
    # form_classes = {"user" : RegisterForm, "customer" : CustomerForm}
    template_name = 'registration/signup.html'
    

    def get(self, request, *args, **kwargs):
        form1 = RegisterForm()
        form2 = CustomerForm()
        context = {
            'form1':form1,
            'form2':form2,
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form1 = RegisterForm(request.POST)
        form2 = CustomerForm(request.POST)
        if form1.is_valid() & form2.is_valid():
            user = form1.save(commit=False)
            customer = form2.save(commit=False)
            customer.user = user
            #set user to inactive until the email confirmation is sent
            # user = request.user
            # user.is_active = False
            user.save()
            customer.save()
            #send confirmation email
            # current_site = get_current_site(request)
            # subject = 'Activate your account'
            # message = render_to_string('registration/account_activate_email.html', {
            #     'user':user,
            #     'domain':current_site.domain,
            #     # 'uid':urlsafe_base64_encode(force_bytes(user.id)).decode(),
            #     'uid':urlsafe_base64_encode(force_bytes(user.id)),
            #     'token':default_token_generator.make_token(user),
            # })
            # user.email_user(subject, message, from_email=None, **kwargs)
            # messages.success(request, 'Please confirm your email to complete registration')
            return redirect('login')
        return render(request, self.template_name, {'form1':form1, 'form2':form2})


class UserLoginView(LoginView):
    template_name = "registration/login.html"

class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect()
    

# def signin(request):
#     return render(request, 'registration/signin.html')


# def signup(request):
#     return render(request, 'registration/signup.html')




# 