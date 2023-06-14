from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'house_hunting_app/base.html')

def signup(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        password = request.POST.get('password') 
        user = User.object.create_user(email=user_email, password=password)
        user.save()
        return render(request, 'house_hunting_app/base.html')
    return render(request, 'house_hunting_app/signup.html')