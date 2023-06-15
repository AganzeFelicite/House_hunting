from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone as timezone
import uuid
 


# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        id = uuid.uuid4()
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.user_id = id
        user.set_password(password)
        user.save(using=self.db)
        return user 
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extra_fields) 
     
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True) 
        return self._create_user(email=email, password=password, **extra_fields)
    
    
class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    houses = models.ManyToManyField('House', related_name='has', blank=True)
    
    def user_profile(self, name, first_name, last_name, phone_no, location_prefered):
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.location_prefered = location_prefered
        self.save(using=self._db)
        return self
        
       
    
    
    
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
    
    
    

class House(models.Model):
    house_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.FloatField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.CharField(max_length=255, default='available')
    date_added = models.DateTimeField(default=timezone.now)
    date_booked = models.DateTimeField(null=True, blank=True)
    house_owner = models.ManyToManyField('User', related_name='has', blank=False)
    
    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = 'House'
        verbose_name_plural = 'Houses'
        
    def update_status(self, status):
        self.status = status
        self.save(using=self._db)
        return self
    def update_date_booked(self, date_booked):
        self.date_booked = date_booked
        self.save(using=self._db)
        return self
    
    def update_house(self, price, location, description, image1, image2, image3):
        self.price = price
        self.location = location
        self.description = description
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.save(using=self._db)
        return self
    
    
    