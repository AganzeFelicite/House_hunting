
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("Account/", views.Account, name="Account"),
    path("logout/", views.logout, name="logout"),
]
