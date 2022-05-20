from .models import Register
from django.forms import ModelForm, TextInput, DateInput, EmailInput, FileInput

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

