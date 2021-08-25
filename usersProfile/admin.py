from django.contrib import admin
from .models import Users
# Register your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'age', 'skills','image1','image2']

