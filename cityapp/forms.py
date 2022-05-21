from .models import Register
from django.forms import ModelForm, TextInput, DateInput, EmailInput, FileInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(ModelForm):

    class Meta:
        model = Register
        fields = ['name', 'surname', 'country', 'desired_city', 'desired_place', 'date', 'card_num', 'email', 'image']

        widgets = {
            "name": TextInput(attrs={
                "class": 'form_control',
                "placeholder": 'Name'
            }),
            "surname": TextInput(attrs={
                "class": 'form_control',
                "placeholder": 'Surname'
            }),
            "country": TextInput(attrs={
                "class": 'form_control',
                "placeholder": 'Country'
            }),
            "desired_city": TextInput(attrs={
                "class": 'form_control',
                "placeholder": 'Desired City'
            }),
            "desired_place": TextInput(attrs={
                "class": 'form_control',
                "placeholder": 'Desired Place'
            }),
            "date": DateInput(
                format=('%d-%m-%Y'),
                attrs={
                "class": 'form_control',
                "type":"date"
            }),
            "card_num": TextInput(attrs={
                "class": 'form_control',
                "placeholder": 'Num of Card'
            }),
            "email": EmailInput(attrs={
                "class": 'form_control',
                "placeholder": 'Your Email'
            }),
            "image": FileInput(attrs={
                "class": 'form_control',
                "placeholder": 'Your Photo'
            })
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

