from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from account import forms


# Create your views here.

class UserRegisterView(View):
    form_class = forms.UserRegistrationForm
    template_name = 'account/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['username'], password=cd['password1'], email=cd['email'])
            messages.success(request, 'You registered successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = forms.UserLoginForm
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You logged in successfully', 'success')
                return redirect('home:home')
            messages.error(request, 'Username or Password wrong', 'warning')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You logged out successfully', 'success')
        return redirect('home:home')
