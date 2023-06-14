from django.contrib import admin
from .models import User
admin.site.register(User)

# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ('field1', 'field2', 'field3')  # Customize the fields to display in the list view

# admin.site.register(User, MyModelAdmin)

# # Register your models here.
# # 