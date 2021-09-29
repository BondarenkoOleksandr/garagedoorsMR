from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


class GoogleLoginView(ListView):
    model = User
    template_name = 'login.html'