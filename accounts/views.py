from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import RegisterForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


# Create your views here.

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/signup.html'

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class()
    #     context = {
    #         'form':form,
    #     }
    #     return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #set user to inactive until the email confirmation is sent
            # user = request.user
            # user.is_active = False
            user.save()
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
        return render(request, self.template_name, {'form':form})


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