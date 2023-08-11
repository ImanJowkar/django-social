from django.shortcuts import render
from django.views import View

from account import forms


# Create your views here.

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        return render(request, 'account/register.html')
