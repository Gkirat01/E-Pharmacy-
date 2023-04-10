from django import forms 
from .models import Image, order, bid #, Register

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields


class signupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'email': 'Email'
        }


class updateProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'date_joined', 'last_login']
        labels = {
            'email': 'Email'
        }


class updateAdminProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'email': 'Email'
        }



class ImageForm(forms.ModelForm): 
    class Meta: 
        model=Image 
        fields='__all__'

class orderMediForm(forms.ModelForm):
    class Meta:
        model=order
        fields= ('name', 'address', 'medi1','quantity1', 'medi2', 'quantity2', 'medi3', 'quantity3', 'prescription')

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model=Register
#         fields= '__all__'

class bidForm(forms.ModelForm):
    class Meta:
        model=bid
        fields= ('bid_price',)