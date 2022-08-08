from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class Registration(UserCreationForm):
    full_name = forms.CharField()
    class Meta:
        model = CustomUser
        fields = ("full_name", "username")
