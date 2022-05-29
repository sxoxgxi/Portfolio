# from django.forms import ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


class MyUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']