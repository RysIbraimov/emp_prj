from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'education': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'education'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'location'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'age'}),
            'job': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'job'}),
            'main_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
        }

