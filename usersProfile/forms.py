from django import forms
from django.forms.fields import ImageField
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = '__all__'
#         labels = {'image1':'Image 1', 'image2':'Image 2'}

class UserForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ('user',)
        # fields = ['name','save_name','age','save_age','skills','save_skills','image1','save_image1','image2','save_image2','is_checkbox2']
        labels = {'image1':'Image 1', 'image2':'Image 2'}
