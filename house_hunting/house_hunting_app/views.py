from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from . models import User, House
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, 'house_hunting_app/index.html')


def login(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        password = request.POST['password']
        user  =  auth.authenticate(email=user_email, password=password)
        if user is not None:
            auth.login(request, user)
            user = User.object.get(email=user_email)
            user_id = user.user_id
            return redirect('/Account/?user_id=' + str(user_id))
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login') 
    return render(request, 'house_hunting_app/login.html')
    
    

def signup(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        password = request.POST.get('password') 
        user = User.object.create_user(email=user_email, password=password)
        
        user.save()
        return render(request, 'house_hunting_app/base.html')
    return render(request, 'house_hunting_app/signup.html')




def Account(request):
    user_id = request.GET.get('user_id')
    user = User.object.get(user_id=user_id)
    houses = House.objects.all()

    return render(request, 'house_hunting_app/Account.html', {'user': user, 'houses': houses})


def logout(request):
    auth.logout(request)
    return redirect('index')