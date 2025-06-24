from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Select, FileInput, EmailInput

from user.models import UserProfile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=25, label="Username")
    email = forms.EmailField(max_length=254, label="Email")
    first_name = forms.CharField(max_length=25, label="First Name")
    last_name = forms.CharField(max_length=25, label="Last Name")
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'city', 'country', 'image']

CITY = [
    ('Istanbul', 'Istanbul'),
    ('Ankara', 'Ankara'),
    ('Izmir', 'Izmir'),
]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'city', 'country', 'image']
        widgets = {
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'city': Select(attrs={'class': 'form-control', 'placeholder': 'city'}, choices=CITY),
            'country': TextInput(attrs={'class': 'form-control', 'placeholder': 'country'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
        }
class UserUpdateForm(UserChangeForm):
    password = None 
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}),
        }
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Eski Şifre',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Eski Şifre'}),
    )
    new_password1 = forms.CharField(
        label='Yeni Şifre',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Şifre'}),
    )
    new_password2 = forms.CharField(
        label='Yeni Şifre Tekrar',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Yeni Şifre Tekrar'}),
    )