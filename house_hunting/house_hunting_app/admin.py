from django.contrib import admin
from .models import User, House
admin.site.register(User)
admin.site.register(House)
# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ('field1', 'field2', 'field3')  # Customize the fields to display in the list view

# admin.site.register(House, MyModelAdmin)

# Register your models here.
# 