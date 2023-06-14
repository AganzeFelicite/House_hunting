from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone as timezone

 


# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user 
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('name', "")
        extra_fields.setdefault('first_name', "")
        extra_fields.setdefault('last_name', "")
        extra_fields.setdefault('phone_no', "")
        extra_fields.setdefault('location_prefered', "")
        return self._create_user(email=email, password=password, **extra_fields) 
     
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) 
        return self._create_user(email=email, password=password, **extra_fields)
    
    def user_profile(self, name, first_name, last_name, phone_no, location_prefered):
        
        return self._create_user(name=name, first_name=first_name, last_name=last_name, phone_no=phone_no, location_prefered=location_prefered)
    
class User(AbstractBaseUser, PermissionsMixin):
    #user_id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=True, default="", unique=True)
    name = models.CharField(max_length=255, blank=True, default="")
    first_name = models.CharField(max_length=255, blank=True, default="")
    last_name = models.CharField(max_length=255, blank=True, default="")
    phone_no = models.CharField(max_length=255, blank=True, default="")
    location_prefered = models.CharField(max_length=255, blank=True, default="")
    is_active = models.BooleanField(default=True)   
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField( default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    
    
    
    object = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email' 
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users' 
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name 