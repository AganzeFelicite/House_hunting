
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('admins/logout/', views.login, name='login'),
    path('admin/', views.login, name='login'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("Account/", views.Account, name="Account"),
    path("Account/<str:pk>", views.Account, name="Account"),
    path("logout/", views.logout, name="logout"),
    path("profile/<str:pk>/", views.profile, name="profile"),
    path("details/<str:pk>/", views.details, name="details"),
    path("details/<str:pk>/<str:user_id>/", views.details, name="details"),
    path('go-back/', views.go_back, name='go_back'),
    path('admins/', admin.site.urls),
    path('admins1/', views.admins1, name='admins1'),
    path('search/', views.search_view, name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

