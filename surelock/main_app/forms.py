from django import forms
from .models import Login




class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'  # or specify the fields you want
