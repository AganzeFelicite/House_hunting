from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from . models import User, House
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, 'house_hunting_app/index.html', {'title': 'Home'})


def login(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        password = request.POST['password']
        user  =  auth.authenticate(email=user_email, password=password)
        
        if user is not None:
            auth.login(request, user)
            user = User.object.get(email=user_email)
            if user.is_superuser:
                return redirect('/admins/', {'title': user.name})
            user_id = user.user_id
            return redirect('/Account/?user_id=' + str(user_id), {'title': "Account-" + user.name})
        else:
            messages.info(request, 'invalid credentials', {'title': 'Login'})
            return redirect('login') 
    return render(request, 'house_hunting_app/login.html', {'title': 'Login'})
    
    

def signup(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        password = request.POST['password'] 
        user = User.object.create_user(email=user_email, password=password)
        
        user.save()
        return redirect('/login/')
    return render(request, 'house_hunting_app/signup.html', {'title': 'Signup'})




def Account(request, pk=None):
    if pk is None:
        user_id = request.GET.get('user_id')
        user = User.object.get(user_id=user_id)
        user.user_id = user_id
        houses = House.objects.all()
        return render(request, 'house_hunting_app/Account.html', {'user': user, 'houses': houses, 'title': 'Account'})
    
    user = User.object.get(user_id=pk)
    user.user_id = pk
    houses = House.objects.all()
    return render(request, 'house_hunting_app/Account.html', {'user': user, 'houses': houses, 'title': 'Account'})


def logout(request):
    auth.logout(request)
    return redirect('index')


def profile(request, pk):
    user = User.object.get(user_id=pk)
    if request.method == 'POST':
        if 'update' in request.POST:
            name = request.POST['name']
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            phone_no = request.POST['phone']
            email = request.POST['email']
        if 'delete' in request.POST:
            user.delete()
            return redirect('signup')

        user.update_User(name=name, first_name=first_name, last_name=last_name, phone_no=phone_no, email=email)
        return redirect('/Account/?user_id=' + str(pk), {'title': "Account-" + user.name})
    
    return render(request, 'house_hunting_app/profile.html', {'user': user, 'title': 'Profile'})
    


def go_back(request):
    previous_page = request.META.get('HTTP_REFERER')
    return redirect(previous_page)

def details(request, pk, user_id=None):
    if user_id is None:
        user_id = request.GET.get('user_id')
        user = User.object.get(user_id=user_id)
        house = House.objects.get(house_id=pk)
        users = house.house_owner.get()
        return render(request, 'house_hunting_app/details.html', {'house': house, 'title': 'Details', 'users': users, 'user': user})
    else:
        
        house = House.objects.get(house_id=pk)
        users = house.house_owner.get()
        return render(request, 'house_hunting_app/details.html', {'house': house, 'title': 'Details', 'users': users})



def admins1(request):
    return redirect('/admins/')


def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = House.objects.filter(location__icontains=query)
    return render(request, 'search_results.html', {'results': results})
