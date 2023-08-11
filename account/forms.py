from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'test@gmail.com'}))
    password1 = forms.CharField(label='password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'password'}))
    password2 = forms.CharField(label='confirm password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'repeat your password password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("This email Already Exist.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("This Username Already Exist.")
        return username

    def clean(self):
        cd = super().clean()
        pass1 = cd.get('password1')
        pass2 = cd.get('password2')
        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError("Password must match.")


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'password'}))
