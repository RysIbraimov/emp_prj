from django import forms
from django.core.exceptions import ValidationError

from .models import User

class UserForm(forms.ModelForm):
    # password_confirm = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username', 'email','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
            # 'password_confirm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password_confirm'}),

        }

        # def clean(self):
        #     cleaned_data = super().clean()
        #     password = cleaned_data.get("password")
        #     password_confirm = cleaned_data.get("password_confirm")
        #
        #     if password != password_confirm:
        #         raise ValidationError('Пароли должны совподать!')
        #     else:
        #         return password



class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password'}),
        }
